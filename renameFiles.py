import os

# Directory containing the captured video files
video_directory = "captured_video"

# Function to rename files with sequential names
def rename_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    file_list = os.listdir(directory)
    file_list.sort()  # Sort the files alphabetically
    count = 0

    for filename in file_list:
        if filename.endswith(".png"):  # Make sure to specify the correct file extension
            new_filename = f"{count:06d}.png"  # Format the new name with leading zeros
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
                count += 1
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")

# Call the function to rename files in the specified directory
rename_files(video_directory)
