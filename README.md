### Bank Ingestion Project---(Day-1)

Overview:
The ingestion system follows an event-driven architecture, where every file uploaded into ADLS triggers an Event Grid event, which is then processed by an Azure Function.
This function validates the event, extracts file details, and pushes ingestion metadata to a Service Bus Queue.

Steps for local setup:
1.Created a new Project.
2.Prepared local.settings.json with connection strings.
3.Used service bus connection strings and queue name.
4.Created Init.py and function.json codes.
5.Installed all the requirements.


Steps for doing the task for day 1:
1.Created ADLS containers
2.Created Service Bus namespace and queue
3.In local system the function has started and it gives Eventgridtrigger
4.Created Function app and Deployed init through local system.
5.Created Event in blob and trigger it using function app
6.Now Upload the data in blob container and then it triggers the event and send message to storage bus.
7.There it shows the data is be ingested.

Workflow of Azure:
1.When a file is uploaded into Azure Data Lake (ADLS)
2.Event Grid detects the upload
3.It triggers an Azure Function
4.The Function reads the event, gets the file name and path
5.Then it sends the details into Azure Service Bus
6.Service Bus shows the ingested data into it.


