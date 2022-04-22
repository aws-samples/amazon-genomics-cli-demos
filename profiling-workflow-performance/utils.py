#!/bin/env python3

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

import boto3


DT_FMTS = [
    '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S.%fZ', 
    '%Y-%m-%dT%H:%M:%S+00:00', '%Y-%m-%dT%H:%M:%S.%f+00:00',
    '%Y-%m-%d %H:%M:%S.%f %z %Z', '%Y-%m-%d %H:%M:%S %z %Z',
]


def parse_datetime(s, fmts = DT_FMTS):
    """Parse datetimes using a list of known formats"""
    for fmt in fmts:
        try:
            dt = datetime.strptime(s, fmt)
            return dt
        except ValueError as e:
            pass
    else:
        raise ValueError(f"unable to parse datetime from '{s}'")


def get_job_resources(job):
    """
    Retrieve job compute resources as a dict from an AWS Batch job description
    
    handles both the DEPRECATED container attributes and the recommended
    key-value list in container.resoureRequirements
    """
    resources = {
        'vcpus': None,
        'memory': None
    }
    
    for resource in resources:
        if job['container'].get(resource):
            resources[resource] = job['container'].get(resource)
        elif job['container'].get('resourceRequirements'):
            for req in job['container'].get('resourceRequirements'):
                if resource.lower().startswith(req['type'].lower()):
                    resources[resource] = int(req['value'])
                    break
    
    return resources


def get_job_descriptions(job_ids, batch=boto3.client('batch')):
    """
    Retreive AWS Batch job descriptions for a list of job_ids
    
    Uses multithreaded concurrency up to a maximum of 10 workers.
    Not recommended for use at scale as you may hit AWS Batch API limits.
    """
    jobs = []
    job_ids_sets = chunks(job_ids, 100)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_jobs = {
            executor.submit(batch.describe_jobs, jobs=job_ids_set): job_ids_set
            for job_ids_set in job_ids_sets
        }

        for future in as_completed(future_jobs):
            try:
                response = future.result()
                jobs += response["jobs"]
            except Exception as e:
                print(f"error retrieving job descriptions: {e}")

    descriptions = {job['jobId']:job for job in jobs}
    return descriptions


def chunks(l, n):
    """split list l into chunks of size n"""
    for i in range(0, len(l), n):
        yield l[i : i + n]