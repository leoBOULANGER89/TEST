# Pull Request

<!--
⚠️ INSTRUCTIONS:
- Complete ALL relevant sections for your PR
- Remove sections that do NOT apply to your change
- Replace placeholders between <...> with your information
- Mark [x] checklist items as you progress
-->

## Change type

<!-- Check all applicable boxes -->

- [ ] 🐛 **Bug fix** (fix for an existing issue)
- [ ] ✨ **Feature** (new functionality)
- [ ] 🧠 **Model** (new ML model or improvement to existing model)
- [ ] 🔧 **Refactoring** (code restructuring without functionality change)
- [ ] 📚 **Documentation** (documentation update only)
- [ ] 🚀 **Performance** (performance improvement)
- [ ] 🧪 **Tests** (added or fixed tests)
- [ ] 🔐 **Security** (security patch)
- [ ] 🐳 **DevOps/Infrastructure** (CI/CD, Docker, configuration)
- [ ] 📦 **Dependencies** (dependencies update)

---

## Description

<!--
Clearly and concisely describe what this PR does.
Include necessary context to understand the changes.
-->

**One-line summary:**  
<Describe the main change in one sentence>

**Detailed context:**  
<Explain why this change is needed, what problem it solves, or what functionality it adds>

**Main changes:**
- <Change 1>
- <Change 2>
- <Change 3>

---

## Related Issues

<!-- Link corresponding GitHub issues or Jira tickets -->

Fixes #<issue_number>  
Related to #<issue_number>

---

## 🧠 ML Models

<!-- ⚠️ MANDATORY SECTION if modifying .pt, .pth, .onnx files -->
<!-- Remove this section if no models are modified -->

### Modified model(s)

- [ ] `car_parts` (segmentation)
- [ ] `car_damages/detector` (YOLOv10)
- [ ] `car_damages/segmentation`
- [ ] `car_damages/classificator`
- [ ] `car_angle` (classification)
- [ ] Other: <specify>

### Performance metrics

<!-- Model Validation workflow will generate an automatic report -->
<!-- Add manual summary here if you have preliminary results -->

| Metric | Previous model | New model | Delta | Improvement? |
|--------|---------------|-----------|-------|---------------|
| mAP@0.5 | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |
| Precision | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |
| Recall | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |
| F1-Score | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |

**Model size:** <XX MB>  
**Inference time (CPU):** <XX ms>

### Changes justification

<!-- Explain why you modified the model -->
<!-- Examples: new dataset, new architecture, optimized hyperparameters, etc. -->

<Describe reasons for model modification>

### Learning document

<Link to document explaining how to train the model.>

---

## 🖥️ API / Backend

<!-- Remove this section if no API/Backend changes -->

### Modified/added endpoints

| Method | Endpoint | Description | Breaking change? |
|--------|----------|-------------|------------------|
| <GET/POST/PUT/DELETE> | `/api/v1/...` | <Description> | ✅ Yes / ❌ No |

### Data schema changes

<!-- If modifying data models or database schema -->

**Before:**
```json
{
  "field": "old_value"
}
```

**After:**
```json
{
  "field": "new_value",
  "new_field": "value"
}
```

### Migration required?

- [ ] ✅ Yes, database migration needed
  - Migration script: `<path/to/migration.sql>`
  - Impact: <Describe impact>
- [ ] ❌ No, migration not required

---

## 🖼️ Frontend / UI

<!-- Remove this section if no UI changes -->

### Screenshots

<!-- Add screenshots to show visual changes -->

**Before:**  
<Screenshot here>

**After:**  
<Screenshot here>

### Responsive design

- [ ] Tested on desktop
- [ ] Tested on tablet
- [ ] Tested on mobile

---

## 📊 OBD-II / Hardware

<!-- Remove this section if no hardware-related changes -->

### Affected hardware

- [ ] OBDLink MX+
- [ ] OBD-II Simulator
- [ ] Other: <specify>

### PIDs used

| PID | Description | Formula | Unit |
|-----|-------------|---------|------|
| `0105` | Coolant Temperature | `A - 40` | °C |
| `010D` | Vehicle Speed | `A` | km/h |
| `0104` | Engine Load | `A * 100 / 255` | % |

### Communication interface

- **Port:** `/dev/rfcomm0`
- **Protocol:** RFCOMM Bluetooth
- **Baud rate:** <if applicable>

---

## 🧪 Tests

### Unit tests

- [ ] I added tests to cover my changes
- [ ] All existing unit tests pass
- [ ] Code coverage: <XX%>

**Command to run tests:**
```bash
pytest tests/
```

### Integration tests

- [ ] I tested integration with other components
- [ ] I tested edge cases

### Manual tests performed

<!-- Describe manual tests you performed -->

1. <Description of test 1>
2. <Description of test 2>
3. <Description of test 3>

---

## 📝 How to test this PR?

<!--
MANDATORY SECTION
Provide CLEAR and DETAILED instructions to test your changes
-->

### Prerequisites

<!-- List everything that must be installed/configured before testing -->

- [ ] <Dependency 1>
- [ ] <Dependency 2>
- [ ] <Specific configuration>

### Step 1: Environment setup

```bash
# Example commands
git checkout <branch>
pip install -r requirements.txt
```

### Step 2: <Step name>

```bash
# Commands or actions to perform
```

**Expected result:**  
<Describe what should happen>

### Step 3: <Step name>

```bash
# Commands or actions to perform
```

**Expected result:**  
<Describe what should happen>

<!-- Add as many steps as needed -->

---

## ✅ Checklist

<!-- Check all applicable boxes. If a box cannot be checked, explain why in comments -->

<!-- Verify GitAction results before checking -->

### Code Quality

- [ ] My code follows project style conventions (PEP 8, Black, isort) <!-- Check Code Linting -->
- [ ] I performed self-review of my code
- [ ] My code is readable and understandable <!-- Check Code Linting -->
- [ ] I commented complex parts of the code
- [ ] I removed debug logs and unnecessary comments

### Documentation

- [ ] I updated relevant documentation
- [ ] I added docstrings to new functions/classes
- [ ] I updated README if needed
- [ ] I documented API changes in changelog

### Tests

- [ ] I added tests that verify my fix works or my functionality works
- [ ] New and existing tests pass locally <!-- Check Unit Tests -->
- [ ] I verified code coverage

### Security

- [ ] I did not introduce known vulnerabilities <!-- Check Dependency Vulnerability Scan -->
- [ ] I did not expose secrets (API keys, passwords, tokens) <!-- Check Bandit Security Scan -->
- [ ] I validated all user inputs
- [ ] I used parameterized queries for SQL queries

### Performance

- [ ] I verified my changes do not have negative performance impact
- [ ] I optimized database queries if applicable
- [ ] I avoided N+1 loops

### Git

- [ ] My commits are descriptive and follow commit convention <!-- Check pre-commit -->
- [ ] I rebased my branch on latest `main`/`development`
- [ ] I resolved all merge conflicts

---

## 🔍 Automated verification results

### Pre-commit Hooks

<!-- Hooks run automatically, document here if you had to skip any -->

- [x] Black (formatting)
- [x] isort (imports)
- [x] Ruff (linting)
- [x] Bandit (security)
- [x] nbstripout (notebooks)

### GitHub Actions

<!-- These verifications run automatically on push -->

#### Lint

<img width="698" alt="Pylint Results" src="<your_screenshot_url>">

**Pylint Score:** <X.XX/10>

#### Tests

```
<Terminal output when testing>
```

**Coverage:** <XX%>

#### Security Scan

<!-- Check Git Action logs -->
- **Bandit:** ✅ No issues detected
- **Snyk:** ✅ No vulnerabilities in dependencies
- **Trivy:** ✅ Docker image secured (if applicable)

---

## 🚨 Breaking Changes

<!-- ⚠️ CRITICAL SECTION if your PR introduces breaking changes -->
<!-- Remove this section if no breaking changes -->

### Incompatible changes

<List all changes that break backward compatibility>

### Actions required for users

1. <Action 1>
2. <Action 2>

### Migration plan

<Describe how to migrate from previous version>

---

## 📌 Additional notes

<!-- Any additional information reviewers should know -->

<Additional information>

---

## 🔗 Resources

<!-- Links to documents, designs, discussions, etc. -->

- Design: <URL>
- Discussion: <URL>
- External documentation: <URL>

---

## 📸 Demo

<!-- (optional) If applicable, add video or GIF demo -->

<Insert GIF or video link>

---

## ⏱️ Time estimate

**Estimated review time:** <XX minutes>  
**Complexity:** 🟢 Low / 🟡 Medium / 🔴 High

---

## 👥 Suggested reviewers

<!-- Mention who should review this PR -->

@<username1> @<username2>

---

<!--
══════════════════════════════════════════════════════════════════════
TEMPLATE END
══════════════════════════════════════════════════════════════════════

Thank you for taking the time to complete this template.
A well-documented PR facilitates review and accelerates merge!
-->
