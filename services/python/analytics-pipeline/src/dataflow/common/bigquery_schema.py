from google.cloud import bigquery

schema_events = [
  bigquery.SchemaField(name = 'analytics_environment', field_type = 'STRING', mode = 'NULLABLE', description = 'Environment derived from the GCS path.'),
  bigquery.SchemaField(name = 'batch_id', field_type = 'STRING', mode = 'NULLABLE', description = 'MD5 hash of the GCS filepath.'),
  bigquery.SchemaField(name = 'event_id', field_type = 'STRING', mode = 'NULLABLE', description = 'The eventId'),
  bigquery.SchemaField(name = 'event_index', field_type = 'INTEGER', mode = 'NULLABLE', description = 'The index of the event within its batch.'),
  bigquery.SchemaField(name = 'event_source', field_type = 'STRING', mode = 'NULLABLE', description = 'Worker type the event originated from.'),
  bigquery.SchemaField(name = 'event_class', field_type = 'STRING', mode = 'NULLABLE', description = 'Higher order category of event.'),
  bigquery.SchemaField(name = 'event_type', field_type = 'STRING', mode = 'NULLABLE', description = 'The eventType.'),
  bigquery.SchemaField(name = 'session_id', field_type = 'STRING', mode = 'NULLABLE', description = 'The sessionId.'),
  bigquery.SchemaField(name = 'build_version', field_type = 'STRING', mode = 'NULLABLE', description = 'The version of the game\'s build.'),
  bigquery.SchemaField(name = 'event_environment', field_type = 'STRING', mode = 'NULLABLE', description = 'The environment the event originated from.'),
  bigquery.SchemaField(name = 'event_timestamp', field_type = 'TIMESTAMP', mode = 'NULLABLE', description = '{partition}The timestamp of the event.'.format(partition = partition)),
  bigquery.SchemaField(name = 'received_timestamp', field_type = 'TIMESTAMP', mode = 'NULLABLE', description = 'The timestamp of when the event was received.'),
  bigquery.SchemaField(name = 'inserted_timestamp', field_type = 'TIMESTAMP', mode = 'NULLABLE', description = 'The timestamp of when the event was ingested into BQ.'),
  bigquery.SchemaField(name = 'job_name', field_type = 'STRING', mode = 'NULLABLE', description = 'The name of the data pipeline or function that ingested the event into BQ.'),
  bigquery.SchemaField(name = 'event_attributes', field_type = 'STRING', mode = 'NULLABLE', description = 'Custom data for the event.')
 ]

schema_logs = [
  bigquery.SchemaField(name = 'job_name', field_type = 'STRING', mode = 'NULLABLE', description = 'Job name.'),
  bigquery.SchemaField(name = 'processed_timestamp', field_type = 'TIMESTAMP', mode = 'NULLABLE', description = 'Time when event file was parsed.'),
  bigquery.SchemaField(name = 'batch_id', field_type = 'STRING', mode = 'NULLABLE', description = 'The batchId.'),
  bigquery.SchemaField(name = 'analytics_environment', field_type = 'STRING', mode = 'NULLABLE', description = 'Analytics environment of the GCS path.'),
  bigquery.SchemaField(name = 'event_category', field_type = 'STRING', mode = 'NULLABLE', description = 'Event category of the GCS path.'),
  bigquery.SchemaField(name = 'event_ds', field_type = 'DATE', mode = 'NULLABLE', description = '{partition}Event ds of the GCS path.'.format(partition = partition)),
  bigquery.SchemaField(name = 'event_time', field_type = 'STRING', mode = 'NULLABLE', description = 'Event time of the GCS path.'),
  bigquery.SchemaField(name = 'event', field_type = 'STRING', mode = 'NULLABLE', description = 'Event'),
  bigquery.SchemaField(name = 'file_path', field_type = 'STRING', mode = 'NULLABLE', description = 'GCS Path of the event file.')
 ]
