# 🐧 Linux Basic Operations - Task Submission

This repository contains a shell script and task breakdown for basic Linux command-line operations. Each task is accompanied by the relevant commands.

---

## ✅ Tasks and Commands

### 1. Creating and Renaming Files/Directories
```bash
mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
cd ..
````

### 2. Viewing File Contents

```bash
cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```

### 3. Searching for Patterns

```bash
grep "root" /etc/passwd
```

### 4. Zipping and Unzipping

```bash
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
```

### 5. Downloading Files

```bash
wget https://example.com/sample.txt
```

### 6. Changing Permissions

```bash
touch secure.txt
chmod 444 secure.txt
```

### 7. Working with Environment Variables

```bash
export MY_VAR="Hello, Linux!"
echo $MY_VAR
```

---

## 🚀 How to Run

Clone the repository and run the script:

```bash
chmod +x linux_tasks.sh
./linux_tasks.sh
```

---

## 📂 File Structure

```
.
├── linux_tasks.sh   # Shell script with all task commands
├── README.md        # This file
```
