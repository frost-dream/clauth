from Crypto.Cipher import AES
import struct
import os

# Define the AES key and IV
aes_key = b"0x29A8DBD15F014D2F97C71B7F04AF1A9F7F18BAAA183D5DE38F003595CDE9607E"
aes_iv = b"0x8ADE56D33B02E931458625C399B34B8B"

# Define a function to decrypt the data using AES
def decrypt_data(data):
    cipher = AES.new(aes_key, AES.MODE_CBC, iv=aes_iv)
    return cipher.decrypt(data)

# Define a function to extract the files from the .pak file
def extract_pak_file(pak_file_path, output_dir):
    with open(pak_file_path, "rb") as pak_file:
        pak_header = pak_file.read(13)
        if pak_header != b"UE3-Pak-File\x0a":
            raise ValueError("Invalid .pak file header")

        # Get the file count and offset
        file_count, pak_offset = struct.unpack("<ii", pak_file.read(8))
        pak_file.seek(pak_offset, os.SEEK_SET)

        # Extract each file
        for i in range(file_count):
            # Read the file header
            file_offset, compressed_size, uncompressed_size = struct.unpack("<qqq", pak_file.read(24))
            file_name_length = struct.unpack("<i", pak_file.read(4))[0]
            file_name = pak_file.read(file_name_length).decode("utf-8")

            # Compute the file padding
            file_data_offset = pak_offset + file_offset
            file_padding = (16 - (file_data_offset % 16)) % 16

            # Read and decrypt the file data
            pak_file.seek(file_data_offset + file_padding, os.SEEK_SET)
            file_data = pak_file.read(compressed_size)
            file_data = decrypt_data(file_data)[:uncompressed_size]

            # Write the file data to disk
            file_path = os.path.join(output_dir, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "wb") as output_file:
                output_file.write(file_data)

# Call the "extract_pak_file" function with the path to the .pak file and the output directory
extract_pak_file("C:/Program Files/Epic Games/Fortnite/FortniteGame/Content/Paks/pakchunk0_s1-WindowsClient.pak", "C:/users/lenovo/desktop")
