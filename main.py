import time
import smtplib

def send_email(subject, body, recipient_list, interval):
    stop_sending = False

    # Sort recipient_list based on hierarchy (if necessary)
    sorted_recipients = sorted(recipient_list, key=lambda recipient: recipient.get('hierarchy', 0))

    # Connect to the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your email server details
    server.starttls()
    server.login('ratheeshraju2003@gmail.com', 'lndzbnurfdzklcdu')  # Replace with your email credentials

    # Prompt the user for input
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    year = input("Enter your year: ")
    college_id = input("Enter your college ID: ")
    block_name = input("Enter your block name: ")
    room_no = input("Enter your room number: ")
    problem = input("Enter the problem description: ")
    media = input("Enter the media (image or video) link: ")
    date = input("Enter the date: ")

    for recipient in sorted_recipients:
        if stop_sending:
            break

        recipient_email = recipient.get('email')

        # Update the recipient dictionary with user input
        recipient.update({'name': name, 'department': department, 'year': year, 'college_id': college_id,
                          'block_name': block_name, 'room_no': room_no, 'problem': problem, 'media': media,
                          'date': date})

        # Check if 'name' key is present in the recipient dictionary
        if 'name' not in recipient:
            print(f"Skipping recipient {recipient_email} due to missing 'name' key")
            continue

        # Compose the email message
        message = f"Subject: {subject}\n\n{body.format(**recipient)}"

        try:
            # Send the email
            server.sendmail('ratheeshraju2003@gmail.com', recipient_email, message)
            print(f"Email sent to: {recipient_email}")

            # Wait for the interval
            time.sleep(interval)

            # Ask if the recipient responded
            response = input("Did the recipient respond to the email? (yes/no): ")

            if response.lower() == "yes":
                stop_sending = True
                print(f"Response received from: {recipient_email}")
            elif response.lower() == "no":
                print(f"No response received from: {recipient_email}. Sending email to the next recipient.")

        except smtplib.SMTPException as e:
            print(f"Failed to send email to: {recipient_email}")
            print(f"Error message: {str(e)}")

        except Exception as e:
            print(f"An error occurred while sending email to: {recipient_email}")
            print(f"Error message: {str(e)}")

    server.quit()


# Example usage
subject = "Maintenance Request"
body = """
Hello,

This is a maintenance request from {name}.

Department: {department}
Year: {year}
College ID: {college_id}
Block Name: {block_name}
Room Number: {room_no}
Date: {date}

Problem Description: {problem}

Media: {media}

Please take the necessary action.

Regards,
Maintenance Team
"""

recipient_list = [
    {'email': 'ratheeshraju2003@gmail.com', 'hierarchy': 1},
    {'email': 'ratheeshraju01@gmail.com', 'hierarchy': 2},
    {'email': 'ratheeshaids@gmail.com', 'hierarchy': 3}
]
interval = 30  # Interval in seconds between each recipient

send_email(subject, body, recipient_list, interval)
