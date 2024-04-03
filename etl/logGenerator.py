import faker
import random
import time



# Generate a log record
def generate_log():
    fake = faker.Faker()

    # Define log levels
    log_levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']

    # Define components
    components = ['backend', 'frontend', 'database', 'messaging_queue', 'etl_pipeline']

    # Define user actions
    user_actions = ['task_completed', 'page_load_error', 'query_executed', 'message_delivery_failure', 'pipeline_completed',
                    'login_failed', 'payment_failed', 'dashboard_accessed', 'report_generated']

    # Define modules for each component
    modules = {
        'backend': ['order_processing', 'user_management', 'inventory_management'],
        'frontend': ['user_management', 'dashboard', 'reporting'],
        'database': ['inventory_management', 'user_management'],
        'messaging_queue': ['notification_service', 'event_processing'],
        'etl_pipeline': ['data_processing', 'data_ingestion']
    }
    timestamp = fake.date_time_this_year().isoformat() + 'Z'  # Current timestamp in ISO 8601 format
    log_level = random.choice(log_levels)
    component = random.choice(components)
    action = random.choice(user_actions)
    module = random.choice(modules[component])
    message = ''
    data = None

    if action == 'task_completed':
        user_id = fake.uuid4()
        data = {
            'order_id': fake.unique.random_number(digits=5),
            'customer_id': fake.unique.random_number(digits=4),
            'total_amount': round(random.uniform(50, 500), 2)
        }
        message = f"Order processing task completed successfully for order {data['order_id']}"
    elif action == 'page_load_error':
        message = "Error loading user profile page"
    elif action == 'query_executed':
        user_id = fake.uuid4()
        data = {
            'item_id': fake.unique.random_number(digits=5),
            'quantity': random.randint(10, 100)
        }
        message = f"Database query executed to update inventory item {data['item_id']}"
    elif action == 'message_delivery_failure':
        data = {
            'user_id': fake.uuid4(),
            'notification_type': random.choice(['email', 'sms']),
            'error_message': "Recipient email address not found"
        }
        message = f"Failed to deliver {data['notification_type']} notification message to user {data['user_id']}"
    elif action == 'pipeline_completed':
        message = "Data processing pipeline completed successfully"
        data = {
            'input_records': random.randint(500, 1000),
            'output_records': random.randint(450, 950),
            'processing_time_ms': random.randint(10000, 30000)
        }
    elif action == 'login_failed':
        data = {
            'user_id': fake.uuid4(),
            'error_message': "Invalid credentials provided"
        }
        message = f"Login attempt failed for user {data['user_id']}: {data['error_message']}"
    elif action == 'payment_failed':
        data = {
            'order_id': fake.unique.random_number(digits=5),
            'error_message': "Insufficient funds"
        }
        message = f"Payment failed for order {data['order_id']}: {data['error_message']}"
    elif action == 'dashboard_accessed':
        user_id = fake.uuid4()
        message = f"Dashboard accessed by user {user_id}"
    elif action == 'report_generated':
        report_id = fake.unique.random_number(digits=2)
        message = f"Report generated: {report_id}"

    if(data is None):
        log_record = {
        'timestamp': timestamp,
        'log_level': log_level,
        'component': component,
        'action': action,
        'module': module,
        'message': message,
    }
    else:
        log_record = {
        'timestamp': timestamp,
        'log_level': log_level,
        'component': component,
        'action': action,
        'user_id': data.get('user_id', None),
        'module': module,
        'message': message,
        'data': data
        }
    return log_record

