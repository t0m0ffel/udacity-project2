

# Bringing Azure ML into Production
This project is all about deployment of azure AutoML models. We covered topic including Authentication, automating ML experiments, enable and viewing logging information, using swagger to interact with the model API, as well as making requests from a python script to the model api.
In the end we also covered the creation, publishing and consumption of azure pipelines.

## Architectural Diagram
![diagram.png](screenshots%2Fdiagram.png)
## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 


* Upload of the Banking Dataset.
![ss2_1_registered_dataset.png.png](screenshots%2Fss2_1_registered_dataset.png)
![ss2_registered_dataset.png](screenshots%2Fss2_registered_dataset.png)

* Creation of the AutoML Pipeline with the Banking Dataset
![ss3_completed_experiment.png](screenshots%2Fss3_completed_experiment.png)

* Selection of the best model
![ss4_best_model.png](screenshots%2Fss4_best_model.png)

* Using *log.py* to enable application insights
![ss5_application_insights.png](screenshots%2Fss5_application_insights.png)

* Run *log.py* in the azure terminal to output the logs (I could not run this on my client. I assume there is a problem with the proxy my company uses.)
![ss5_application_insights.png](screenshots%2Fss5_application_insights.png)

* Download the swagger file form the endpoint and run the provided scripts to view it locally in the browser
![ss7_swagger.png](screenshots%2Fss7_swagger.png)

* Modify the *endpoint.py* by adding URL and primary key to make a request with the sample payload
![ss8_endpoint_test.png](screenshots%2Fss8_endpoint_test.png)

* Add the project name to the provided Notebook to create, run and schedule the pipeline
![ss9_pipeline_creation.png](screenshots%2Fss9_pipeline_creation.png)
![ss10_pipeline_section.png](screenshots%2Fss10_pipeline_section.png)
![ss11_data_and_automl_module.png](screenshots%2Fss11_data_and_automl_module.png)
![ss12_published_pipeline.png](screenshots%2Fss12_published_pipeline.png)
![ss13_rundetails_widget.png](screenshots%2Fss13_rundetails_widget.png)
![ss14_scheduled_run.png](screenshots%2Fss14_scheduled_run.png)


## Screen Recording
https://www.youtube.com/watch?v=Y1zAGJDcHtk

Description:
1. I show the published endpoint for the model and use the new feature were we can test payload within the browser. For this I use the payload provided in the *endpoint.py*
2. Then I show the pipline created by the provided Notebook.
3. Next I show the best model created by AutoML
4. Last I show an example run of *endpoint.py* on my client with the sample payload which produces the same result mentioned in step 1.

## Standout Suggestions

Class imbalance: Since the target labels are very imbalanced (8872 no and 1128 yes) we could use the techniques of over or under sampling to improve our model. These are proven methods which can deal with exactly this problem.

To speed up the model prediction time we could use [batch inference pipelines](https://learn.microsoft.com/en-us/training/modules/deploy-batch-inference-pipelines-with-azure-machine-learning/). 
This pipeline can be published for our trained model and then used to generate predictions asynchronously more quickly for larger requests.