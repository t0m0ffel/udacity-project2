

# Bringing Azure ML into Production
This project is all about deployment of azure AutoML models. We covered topic including Authentication, automating ML experiments, enable and viewing logging information, using swagger to interact with the model API, as well as making requests from a python script to the model api.
In the end we also covered the creation, publishing and consumption of azure pipelines.

In this project we use again the bank marketing data which is about a marketing campaign and how customers responded to it (positive or negative).
This makes it perfect for a binary classification task which is well-supported by Azure AutoML. So we uploaded the dataset to azure and set up a AutoML task with the dataset.
After finding the best model we published the model via the azure endpoint feature, interacted with it (via swagger and a script) and had a peek into the logs.
Finally, we used the provided notebook to publish a AutoML pipeline with the same dataset which was also accessible by a published endpoint.


## Architectural Diagram
![diagram.png](screenshots%2Fdiagram.png)
## Key Steps


### Upload of the Banking Dataset
Here we can se the uploaded datasets including some meta information. In the detail page we also can see how we can consume it in a notebook with some sample code as well as models which were trained on the dataset.

![ss2_1_registered_dataset.png](screenshots%2Fss2_1_registered_dataset.png)
![ss2_registered_dataset.png](screenshots%2Fss2_registered_dataset.png)


### Creation of the AutoML Pipeline with the Banking Dataset
On this page we can see an overview of the AutoML job we started on the banking dataset with some meta information e.g. the cluster we ran it on.
Furthermore, we see already the best model produced by the AutoML run (in this case Voting Ensemble).
![ss3_completed_experiment.png](screenshots%2Fss3_completed_experiment.png)

### Selection of the best model
On this page we see details about the best model. We could see further models explanations and metrics here in the appropriated tabs.
![ss4_best_model.png](screenshots%2Fss4_best_model.png)

### Using *log.py* to enable application insights
On this page we can see details about the published endpoint. Since the endpoint is not ready yet the URL and swagger config is missing.
Furthermore, we can that application insights are enabled, which we did through a command in the *logs.py* file.
![ss5_application_insights.png](screenshots%2Fss5_application_insights.png)

### Run *log.py* in the azure terminal to output the logs 
Here we can see the output of the logging of the endpoint using *log.py* in azure console.
![ss6_python_logs.png](screenshots%2Fss6_python_logs.png)


Here we see the same using the local console in the provided vm.

![ss6_2_python_logs.png](screenshots%2Fss6_3_python_logs.png)


### Download the swagger file form the endpoint and run the provided scripts to view it locally in the browser
Here we can see the downloaded swagger file running on localhost. Most importantly we can see an example request. And can try out the endpoints here before using them in our code.
![ss7_swagger.png](screenshots%2Fss7_swagger.png)

### Modify the *endpoint.py* by adding URL and primary key to make a request with the sample payload
Here we see just the result of a sample request executed on my local machine and the result from the model endpoint.
![ss8_endpoint_test.png](screenshots%2Fss8_endpoint_test.png)

### Add the project name to the provided Notebook to create, run and schedule the pipeline
We used the notebook to create, run and schedule the pipeline

On the first image we see an overview of all pipeline jobs with current status. On this screenshot we can see that all jobs are completed

[//]: # (![ss9_pipeline_creation.png]&#40;screenshots%2Fss9_pipeline_creation.png&#41;)
![ss10_pipeline_section.png](screenshots%2Fss10_pipeline_section.png)

On this image we can see the pipeline endpoint for our Bankmarketing Train Pipeline.
![pipeline_overview.png](screenshots%2Fpipeline_overview.png)
On this image we can see the details of pipeline job. In our simple example we just feed the created Bankmarketing dataset into
the automl module
![ss11_data_and_automl_module.png](screenshots%2Fss11_data_and_automl_module.png)
Here we can see the pipeline endpoint together with the REST url which we can use in our application to access the pipeline.
![ss12_published_pipeline.png](screenshots%2Fss12_published_pipeline.png)
This screenshot shows the details of our pipeline run. It displays the graph with the dataset and the automl module as we have seen before.
Furthermore, it gives us metadata for the run such as start adn end time.
![ss13_rundetails_widget.png](screenshots%2Fss13_rundetails_widget.png)
Lastly, we see an overview of all the jobs and see that all are completed.
![ss14_scheduled_run.png](screenshots%2Fss14_scheduled_run.png)


## Screen Recording
https://www.youtube.com/watch?v=hqOY8KSK6nc

Description:
1. I show the published endpoint for the model and use the new feature were we can test payload within the browser. For this I use the payload provided in the *endpoint.py*
2. Then I show the pipline created by the provided Notebook.
3. Next I show the best model created by AutoML
4. Last I show an example run of *endpoint.py* on my client with the sample payload which produces the same result mentioned in step 1.

## Standout Suggestions

Class imbalance: Since the target labels are very imbalanced (8872 no and 1128 yes) we could use the techniques of over or under sampling to improve our model. These are proven methods which can deal with exactly this problem.

To speed up the model prediction time we could use [batch inference pipelines](https://learn.microsoft.com/en-us/training/modules/deploy-batch-inference-pipelines-with-azure-machine-learning/). 
This pipeline can be published for our trained model and then used to generate predictions asynchronously more quickly for larger requests.