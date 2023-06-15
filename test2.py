import time
import smtplib
import datetime
import tkinter as tk
from tkinter import messagebox

def send_email(subject, body, recipient_list, interval):
    stop_sending = False

    # Sort recipient_list based on hierarchy (if necessary)
    sorted_recipients = sorted(recipient_list, key=lambda recipient: recipient.get('hierarchy', 0))

    try:
        # Connect to the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your email server details
        server.starttls()
        server.login('ratheeshraju2003@gmail.com', 'lndzbnurfdzklcdu')  # Replace with your email credentials

        for recipient in sorted_recipients:
            if stop_sending:
                break

            recipient_email = recipient.get('email')

            # Check if all required keys are present in the recipient dictionary
            required_keys = ['name', 'department', 'year', 'college_id', 'block_name', 'room_no', 'problem', 'media', 'date']
            if not all(key in recipient for key in required_keys):
                messagebox.showwarning("Missing Information", f"Skipping recipient {recipient_email} due to missing keys.")
                continue

            # Compose the email message
            message = f"Subject: {subject}\n\n{body.format(**recipient)}"

            try:
                # Send the email
                server.sendmail('ratheeshraju2003@gmail.com', recipient_email, message)
                messagebox.showinfo("Email Sent", f"Email sent to: {recipient_email}")

                # Create and start the timer
                timer_label = tk.Label(window, text="", font=("Arial", 72), bg="#FFAF00")
                timer_label.place(relx=0.5, rely=0.5, anchor="center")

                end_time = datetime.datetime.now() + datetime.timedelta(seconds=interval)
                while datetime.datetime.now() < end_time:
                    remaining_time = end_time - datetime.datetime.now()
                    timer_label.config(text=str(remaining_time).split(".")[0])
                    window.update()
                    time.sleep(1)

                # Remove the timer label
                timer_label.destroy()

                # Ask if the recipient responded
                response = messagebox.askquestion("Recipient Response", "Did the recipient respond to the email?")

                if response.lower() == "yes":
                    stop_sending = True
                    messagebox.showinfo("Response Received", f"Response received from: {recipient_email}")
                elif response.lower() == "no":
                    messagebox.showinfo("No Response", f"No response received from: {recipient_email}. Sending email to the next recipient.")

            except smtplib.SMTPException as e:
                messagebox.showerror("Email Error", f"Failed to send email to: {recipient_email}\nError message: {str(e)}")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while sending email to: {recipient_email}\nError message: {str(e)}")

    except smtplib.SMTPException as e:
        messagebox.showerror("Email Server Error", f"Failed to connect to the email server.\nError message: {str(e)}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while connecting to the email server.\nError message: {str(e)}")

    finally:
        try:
            server.quit()
        except:
            pass


def send_email_ui():
    # Get the input from the user interface
    name = name_entry.get()
    department = department_entry.get()
    year = year_entry.get()
    college_id = college_id_entry.get()
    block_name = block_name_entry.get()
    room_no = room_no_entry.get()
    problem = problem_text.get("1.0", "end-1c")  # Retrieve the text from the text widget
    media = media_entry.get()
    date = date_entry.get()

    # Update all recipient dictionaries with user input values
    for recipient in recipient_list:
        recipient.update({'name': name, 'department': department, 'year': year, 'college_id': college_id,
                          'block_name': block_name, 'room_no': room_no, 'problem': problem, 'media': media,
                          'date': date})

    # Call the send_email function
    send_email(subject, body, recipient_list, interval)

# Example usage
subject = "Complaint Request"
body = """
Hello,

This is a Complaint request from {name}.

Department: {department}
Year: {year}
College ID: {college_id}
Block Name: {block_name}
Room Number: {room_no}
Date: {date}

Problem Description:
{problem}

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
interval = 10 # Interval in seconds between each recipient

# Create the Tkinter window
window = tk.Tk()
window.title("SNSCE BOYS HOSTEL")
window.geometry("400x1000")

# Set the border radius percentage
border_radius_percentage = 50

# Calculate the border radius value
border_radius = int(window.winfo_width() * border_radius_percentage / 100)

# Set the background color
window.configure(bg="#FFAF00")

# Increase font size
font = ("Arial", 14)

# Calculate the width as a percentage of the window width
entry_width = int(window.winfo_width() * 20)

# Create labels and entry fields for user input
date_label = tk.Label(window, text="Date:", font=font, bd=border_radius, bg="#FFAF00")
date_label.pack()
date_entry = tk.Entry(window, font=font)
date_entry.pack(pady=5)
date_entry.config(width=entry_width)

name_label = tk.Label(window, text="Name:", font=font, bd=border_radius, bg="#FFAF00")
name_label.pack()
name_entry = tk.Entry(window, font=font, bd=border_radius)
name_entry.pack(pady=5)
name_entry.config(width=entry_width)

department_label = tk.Label(window, text="Department:", font=font, bd=border_radius, bg="#FFAF00")
department_label.pack()
department_entry = tk.Entry(window, font=font, bd=border_radius)
department_entry.pack(pady=5)
department_entry.config(width=entry_width)

year_label = tk.Label(window, text="Year:", font=font, bd=border_radius, bg="#FFAF00")
year_label.pack()
year_entry = tk.Entry(window, font=font, bd=border_radius)
year_entry.pack(pady=5)
year_entry.config(width=entry_width)

college_id_label = tk.Label(window, text="College ID:", font=font, bd=border_radius, bg="#FFAF00")
college_id_label.pack()
college_id_entry = tk.Entry(window, font=font, bd=border_radius)
college_id_entry.pack(pady=5)
college_id_entry.config(width=entry_width)

block_name_label = tk.Label(window, text="Block Name:", font=font, bd=border_radius, bg="#FFAF00")
block_name_label.pack()
block_name_entry = tk.Entry(window, font=font, bd=border_radius)
block_name_entry.pack(pady=5)
block_name_entry.config(width=entry_width)

room_no_label = tk.Label(window, text="Room Number:", font=font, bd=border_radius, bg="#FFAF00")
room_no_label.pack()
room_no_entry = tk.Entry(window, font=font, bd=border_radius)
room_no_entry.pack(pady=5)
room_no_entry.config(width=entry_width)

problem_label = tk.Label(window, text="Problem Description:", font=font, bd=border_radius, bg="#FFAF00")
problem_label.pack()
problem_text = tk.Text(window, font=font, width=entry_width, height=5, wrap="word")
problem_text.pack(pady=5)

media_label = tk.Label(window, text="Media:", font=font, bd=border_radius, bg="#FFAF00")
media_label.pack()
media_entry = tk.Entry(window, font=font, bd=border_radius)
media_entry.pack(pady=5)
media_entry.config(width=entry_width)

send_button = tk.Button(window, text="Send Email", font=font, command=send_email_ui)
send_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()