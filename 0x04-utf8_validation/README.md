# 0x04. UTF-8 Validation

## 📝 Description

This project implements a UTF-8 validation algorithm that determines if a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding that can encode any character in the Unicode standard.

This challenge focuses on bit manipulation, understanding encoding standards, and data validation techniques.

## 🎯 Learning Objectives

- Understand UTF-8 encoding principles and bit patterns
- Master bitwise operations and bit manipulation in Python
- Learn to validate data according to established standards
- Practice pattern recognition in binary data

## 📋 Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable

## 🚀 Implementation

### Function Prototype
```python
def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding
    
    Args:
        data (List[int]): List of integers representing bytes
        
    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise
    """
```

## 🔍 UTF-8 Encoding Rules

UTF-8 uses 1-4 bytes to encode characters:

### 1-Byte Characters (ASCII - 0-127)
```
0xxxxxxx
```
- Bit pattern: `0xxxxxxx`
- Range: 0x00 to 0x7F

### 2-Byte Characters (128-2047)
```
110xxxxx 10xxxxxx
```
- First byte: `110xxxxx`
- Continuation byte: `10xxxxxx`

### 3-Byte Characters (2048-65535)
```
1110xxxx 10xxxxxx 10xxxxxx
```
- First byte: `1110xxxx`
- Two continuation bytes: `10xxxxxx`

### 4-Byte Characters (65536-1114111)
```
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```
- First byte: `11110xxx`
- Three continuation bytes: `10xxxxxx`

## 📁 Files

| File | Description |
|------|-------------|
| `0-validate_utf8.py` | Main UTF-8 validation implementation |
| `0-main.py` | Test file with sample data |
| `README.md` | Project documentation and usage guide |

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test UTF-8 validation implementation
"""
validUTF8 = __import__('0-validate_utf8').validUTF8

# Test cases
test_cases = [
    [65],                                    # Valid: 'A'
    [80, 121, 116, 104, 111, 110],          # Valid: 'Python'
    [229, 65, 127, 256],                    # Invalid: contains >255
    [197, 130, 1],                          # Valid: 2-byte + ASCII
    [235, 140, 4]                           # Invalid: incomplete sequence
]

for i, data in enumerate(test_cases):
    result = validUTF8(data)
    print(f"Test {i+1}: {data} -> {result}")
```

## 🔍 Algorithm Explanation

### Step-by-Step Validation:

1. **Initialize**: Set `byte_count = 0` to track continuation bytes needed

2. **For each byte in data**:
   - If `byte_count == 0` (expecting a new character):
     - Check if it's a 1-byte char: `0xxxxxxx`
     - Check if it's start of 2-byte: `110xxxxx` → set `byte_count = 1`
     - Check if it's start of 3-byte: `1110xxxx` → set `byte_count = 2`
     - Check if it's start of 4-byte: `11110xxx` → set `byte_count = 3`
     - If none match and it starts with `1`, return `False`
   
   - If `byte_count > 0` (expecting continuation byte):
     - Check if byte matches `10xxxxxx` pattern
     - If not, return `False`
     - Decrement `byte_count`

3. **Return**: `byte_count == 0` (all sequences complete)

### Bit Manipulation Techniques:

```python
# Check if byte starts with '110' (2-byte character start)
if i >> 5 == 0b110:  # Right shift 5 bits, compare with 110

# Check if byte starts with '10' (continuation byte)
if i >> 6 == 0b10:   # Right shift 6 bits, compare with 10

# Check if byte starts with '0' (1-byte character)
if i >> 7 == 0:      # Right shift 7 bits, should be 0
```

## 🔍 Algorithm Complexity

- **Time Complexity:** O(n) - Single pass through the data
- **Space Complexity:** O(1) - Constant extra space

## 💡 Key Concepts

### Bit Manipulation Operations:
- **Right Shift (`>>`)**: Extract specific bit patterns
- **Bitwise AND (`&`)**: Mask specific bits
- **Binary Literals (`0b`)**: Direct binary representation

### UTF-8 Validation Patterns:
```python
# Patterns for different UTF-8 byte types
0b0xxxxxxx  # 1-byte character (ASCII)
0b110xxxxx  # 2-byte character start  
0b1110xxxx  # 3-byte character start
0b11110xxx  # 4-byte character start
0b10xxxxxx  # Continuation byte
```

## 🧮 Examples Breakdown

**Example 1: Valid ASCII**
```
Data: [65]  # 'A'
Binary: 01000001
Pattern: 0xxxxxxx ✓
Result: True
```

**Example 2: Valid 2-byte sequence**
```
Data: [197, 130]  # 'Å'
Binary: 11000101 10000010
Patterns: 110xxxxx 10xxxxxx ✓
Result: True
```

**Example 3: Invalid sequence**
```
Data: [229, 65, 127, 256]
Issue: 256 > 255 (not a valid byte)
Result: False
```

## ✅ Testing

Run comprehensive tests:

```bash
# Test the implementation
python3 0-main.py

# Additional testing
python3 -c "
validUTF8 = __import__('0-validate_utf8').validUTF8

# Test various cases
test_cases = [
    ([65], 'ASCII A'),
    ([197, 130], '2-byte char'),
    ([229, 65, 127, 256], 'Invalid byte > 255'),
    ([240, 159, 152, 128], '4-byte emoji'),
    ([145], 'Invalid start byte')
]

for data, description in test_cases:
    result = validUTF8(data)
    print(f'{description}: {result}')
"
```

## 🚨 Edge Cases

1. **Empty data**: Should return `True`
2. **Bytes > 255**: Invalid (UTF-8 uses 8-bit bytes)
3. **Incomplete sequences**: Missing continuation bytes
4. **Invalid start bytes**: Bytes starting with `10xxxxxx`
5. **Overlong encoding**: Using more bytes than necessary

## 🔗 Related Concepts

- **Character Encoding**: UTF-8, UTF-16, ASCII
- **Bit Manipulation**: Shifting, masking, pattern matching  
- **Data Validation**: Input sanitization and format checking
- **Unicode Standard**: Character representation systems

## 📚 Resources

- [UTF-8 Specification (RFC 3629)](https://tools.ietf.org/html/rfc3629)
- [Unicode Standard](https://unicode.org/standard/standard.html)
- [Python Bitwise Operations](https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations)
- [Character Encoding Guide](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
