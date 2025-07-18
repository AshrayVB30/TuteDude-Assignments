#!/bin/bash

# 1. Creating and Renaming Files/Directories
mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
cd ..

# 2. Viewing File Contents
echo "---- Full /etc/passwd ----"
cat /etc/passwd

echo "---- First 5 lines ----"
head -n 5 /etc/passwd

echo "---- Last 5 lines ----"
tail -n 5 /etc/passwd

# 3. Searching for Patterns
echo "---- Lines with 'root' ----"
grep "root" /etc/passwd

# 4. Zipping and Unzipping
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir

# 5. Downloading Files
wget https://example.com/sample.txt

# 6. Changing Permissions
touch secure.txt
chmod 444 secure.txt

# 7. Working with Environment Variables
export MY_VAR="Hello, Linux!"
echo "MY_VAR is set to: $MY_VAR"


# Make the script executable:
chmod +x linux_tasks.sh

# Run it
./linux_tasks.sh


