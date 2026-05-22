<div align="center">

<!-- ANIMATED HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=Python%20Explorations&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=A%20Hands-On%20Tour%20of%20Core%20Concepts&descAlignY=58&descSize=18&descColor=a78bfa&animation=fadeIn" width="100%"/>

<!-- TYPING ANIMATION -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A78BFA&center=true&vCenter=true&width=600&lines=Run+it.+Tweak+it.+Learn+it.;Numbers%2C+Types%2C+Operators+%E2%80%94+all+here.;No+dependencies.+Just+Python.;Great+for+beginners+%26+interview+prep." alt="Typing SVG" />
</a>

<br/>

<!-- BADGES -->
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-a78bfa?style=for-the-badge&logo=open-access&logoColor=white)
![MIT License](https://img.shields.io/badge/License-Open%20Study-f59e0b?style=for-the-badge&logo=bookstack&logoColor=white)

</div>

---

## ✨ What Makes This Repo Different

> **No fluff. No bloated frameworks. No confusing abstractions.**  
> Just clean, focused Python files you can open, run, and _actually understand_.

Every script in this repo is built around a **single idea** — small enough to hold in your head, clear enough to learn from in minutes.

```python
# That moment when it just clicks 💡
>>> 0b1010 & 0b1100
8
>>> bin(8)
'0b1000'
```

---

## 🗂️ Project Structure

```
Python-Explorations/
│
├── 📁 Base Conversion/
│   ├── Int.py            → integers, bases 2/8/10/16
│   ├── Float.py          → floating point representation
│   ├── Complex.py        → complex numbers demystified
│   └── Conversions.py    → int ↔ str ↔ float ↔ hex ↔ bin
│
├── 📁 Data Types/
│   ├── List.py           → indexing, slicing, mutation
│   ├── Set.py            → uniqueness, unions, intersections
│   ├── Dict.py           → keys, values, comprehensions
│   ├── String.py         → formatting, methods, f-strings
│   └── None.py           → NoneType, identity checks
│
└── 📁 Operators/
    ├── Arithmetic.py     → +, -, *, /, //, %, **
    ├── Bitwise.py        → &, |, ^, ~, <<, >>
    ├── Logical.py        → and, or, not, short-circuit eval
    ├── Relational.py     → ==, !=, <, >, is, in
    └── Division.py       → true vs floor division, modulo edge cases
```

---

## 🚀 Quick Start

> Requires **Python 3.x** — no pip installs, no virtual envs, no setup.

```bash
# Clone it
git clone https://github.com/your-username/DSA-in-Python.git
cd DSA-in-Python

# Pick any file and run it
python "Operators/Bitwise.py"
python "Base Conversion/Int.py"
python "Data Types/String.py"
```

**Tip for Windows users:** Wrap paths with spaces in quotes — e.g. `"Base Conversion/Int.py"`

---

## 🧠 Concept Coverage at a Glance

| Area | Topics Covered | Great For |
|------|---------------|-----------|
| **Base Conversion** | Binary, octal, hex, floats, complex, casting | Understanding how Python stores numbers |
| **Data Types** | Lists, sets, dicts, strings, NoneType | Core data structures, mutation vs immutability |
| **Operators** | Arithmetic, bitwise, logical, relational, division | Interviews, logic problems, low-level thinking |

---

## 💡 How to Get the Most Out of This

The best way to use this repo isn't just to read — it's to **break things on purpose**.

1. **Run a file** to see the default output.
2. **Change a value** — an operand, a data structure, a type.
3. **Predict what happens** before you re-run.
4. **Compare** your prediction with the output.

```python
# In Operators/Bitwise.py — try changing these values and re-running:
a = 0b1010   # ← change me
b = 0b1100   # ← change me too

print(f"AND : {a & b} = {bin(a & b)}")
print(f"OR  : {a | b} = {bin(a | b)}")
print(f"XOR : {a ^ b} = {bin(a ^ b)}")
```

---

## 👥 Who This Is For

<table>
<tr>
<td align="center" width="33%">

### 🐍 New Learners
Just started Python? These files give you real, runnable examples without overwhelming setup or theory. Pick a topic, run it, modify it.

</td>
<td align="center" width="33%">

### 🎯 Interview Preppers
Bitwise tricks, floor division edge cases, and type conversion gotchas come up constantly. Run these files to build that muscle memory fast.

</td>
<td align="center" width="33%">

### 🏫 Teachers & Mentors
Each file is a self-contained demo — perfect for live coding in class, paste-and-explain exercises, or quick concept checks.

</td>
</tr>
</table>

---

## 🔥 Sample Outputs (Sneak Peek)

<details>
<summary><b>Operators/Bitwise.py</b> — click to expand</summary>

```
a = 10  (0b1010)
b = 12  (0b1100)

AND  : 8   → 0b1000
OR   : 14  → 0b1110
XOR  : 6   → 0b0110
NOT a: -11
LEFT SHIFT  (a << 1): 20
RIGHT SHIFT (a >> 1): 5
```
</details>

<details>
<summary><b>Base Conversion/Int.py</b> — click to expand</summary>

```
Decimal  255  → Binary  : 0b11111111
Decimal  255  → Octal   : 0o377
Decimal  255  → Hex     : 0xff

int('ff', 16)  = 255
int('1010', 2) = 10
int('0o17', 8) = 15
```
</details>

<details>
<summary><b>Operators/Division.py</b> — click to expand</summary>

```
7 / 2   = 3.5      ← true division (float)
7 // 2  = 3        ← floor division (int)
7 % 2   = 1        ← remainder
-7 // 2 = -4       ← floors toward -∞, not 0 (!)
```
</details>

---

## 🤝 Contributing

Small, focused PRs are genuinely welcome. Here's what fits best:

- 📝 Clearer inline comments or edge case explanations
- ➕ Additional example values that reveal surprising behavior  
- 🧪 Short `assert`-based tests that double as documentation
- 📂 New compact files for topics not yet covered (e.g. `Walrus.py`, `Unpacking.py`)

**Please keep the spirit of the repo:** one concept, one file, runnable in seconds.

---

## 📄 License

Open for study and reuse. Open an issue if you want help expanding examples or adding a new topic area.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer&animation=fadeIn" width="100%"/>

**Made for curious minds. Run something now. ⚡**

[![Star this repo](https://img.shields.io/badge/⭐_Star_this_repo-if_it_helped_you-f59e0b?style=for-the-badge)](https://github.com/your-username/python-explorations)

</div>
