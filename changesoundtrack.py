import os

# Prompt user to choose one of the six options
print("Please choose one of the following options:")
print("1. Cave Story Arranged (DM DOKURO)")
print("2. Famitracks (Cave Story+ Switch)")
print("3. New (Cave Story WiiWare)")
print("4. Remastered (Cave Story 3D)")
print("5. Ridiculon (Cave Story+ Switch)")
print("6. SNES (Vince94)")
choice = input("Enter the number of your choice: ")

# Set the chosen option as the new text to be written to the file
if choice == "1":
    new_text = "Cave Story Arranged (DM DOKURO)"
elif choice == "2":
    new_text = "Famitracks (Cave Story+ Switch)"
elif choice == "3":
    new_text = "New (Cave Story WiiWare)"
elif choice == "4":
    new_text = "Remastered (Cave Story 3D)"
elif choice == "5":
    new_text = "Ridiculon (Cave Story+ Switch)"
elif choice == "6":
    new_text = "SNES (Vince94)"
else:
    print("Invalid choice. Exiting script.")
    exit()

# Open the settings.ini file and read the lines into a list
file_path = "C:\\Program Files (x86)\\Cave Story Deluxe\\CaveStory\\mods\\alternate_music\\settings.ini"
with open(file_path, "r") as f:
    lines = f.readlines()

# Replace the second line with the new text
lines[1] = "playlist = {}\n".format(new_text)

# Write the modified lines back to the file
with open(file_path, "w") as f:
    f.writelines(lines)

print("Text successfully replaced in file.")
