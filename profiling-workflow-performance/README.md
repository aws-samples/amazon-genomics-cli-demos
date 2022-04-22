# Profiling workflow with the Amazon Genomics CLI

Profiling is an essential part of developing genomics workflows. By identifying and eliminating expensive bottlenecks, users can make workflow performant and cost efficient. A common way to profile a workflow is to generate a timing chart of all tasks executed. The [Amazon Genomics CLI](https://aws.amazon.com/genomics-cli/) (AGC) provides a unified experience for running workflows across [multiple workflow engines](https://aws.github.io/amazon-genomics-cli/docs/concepts/engines/). In doing so, it also enables a common way to generate timing charts and profile workflows.

The [demo notebook here](./profiling_workflow_performance_with_amazon_genomics_cli.ipynb) provides example code that demonstrates how to profile workflows run by the Amazon Genomics CLI as described by the blog "Profiling workflow performance with the Amazon Genomics CLI".

**Note:** The plots in the demo notebook are generated using Bokeh. Github's Jupyter Notebook preview may not render them. For a preview these plots have been exported as html and png:

| plot | html | png |
| --- | :---: | :---: |
| Plot 1 - basic task timing plot | [html](./gatk4-data-processing__onDemandCtxCromwell__8cf8e737-6584-4309-ab5f-0aae8e885369__plot1.html) | [png](./plot1.png) |
| Plot 2 - combined cost, compute resources, and task timing | [html](./gatk4-data-processing__onDemandCtxCromwell__8cf8e737-6584-4309-ab5f-0aae8e885369__plot2.html) | [png](./plot2.png) |
