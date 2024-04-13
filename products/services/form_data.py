from google.cloud import pubsub_v1




def publication_update(id_client,confrmed_updated):
    # TODO(developer)
    project_id = "alpinebank"
    topic_id = "my-topic"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)

    
    data_str = "update client,"+str(id_client)+",isConfirmed set to,"+str(confrmed_updated)
    print(data_str)
    # Data must be a bytestring
    data = data_str.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f"Published messages to {topic_path}.")
    
def publication_escalation():
     # TODO(developer)
    project_id = "alpinebank"
    topic_id = "my-topic"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)

    for n in range(1, 1000):
        data_str = f"Message number {n}"
        # Data must be a bytestring
        data = data_str.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())

    print(f"Published messages to {topic_path}.")
    
    
publication_escalation()