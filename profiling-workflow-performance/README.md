# Profiling workflow with the Amazon Genomics CLI

Profiling is an essential part of developing genomics workflows. By identifying and eliminating expensive bottlenecks, users can make workflow performant and cost efficient. A common way to profile a workflow is to generate a timing chart of all tasks executed. The [Amazon Genomics CLI](https://aws.amazon.com/genomics-cli/) (AGC) provides a unified experience for running workflows across [multiple workflow engines](https://aws.github.io/amazon-genomics-cli/docs/concepts/engines/). In doing so, it also enables a common way to generate timing charts and profile workflows.

The [demo notebook here](./profiling_workflow_performance_with_amazon_genomics_cli.ipynb) provides example code that demonstrates how to profile workflows run by the Amazon Genomics CLI as described by the blog "Profiling workflow performance with the Amazon Genomics CLI".
