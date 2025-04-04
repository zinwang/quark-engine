<p align="center">
    <a href="https://www.blackhat.com/asia-24/arsenal/schedule/index.html#quark-script---dig-vulnerabilities-in-the-blackbox-37549">
        <img alt="Black Hat Arsenal" src="https://img.shields.io/badge/Black%20Hat%20Arsenal-Asia%202024-blue">
    </a>
    <a href="https://www.blackhat.com/asia-21/arsenal/schedule/index.html#quark-engine-storyteller-of-android-malware-22458">
        <img alt="Black Hat Arsenal" src="https://img.shields.io/badge/Black%20Hat%20Arsenal-Asia%202021-blue">
    </a>
    <a href="https://conference.hitb.org/hitb-lockdown002/sessions/quark-engine-an-obfuscation-neglect-android-malware-scoring-system/">
        <img alt="HITB" src="https://img.shields.io/badge/HITB-Lockdown%20002-red">
    </a>
    <a href="https://www.youtube.com/watch?v=XK-yqHPnsvc&ab_channel=DEFCONConference">
        <img alt="defcon" src="https://img.shields.io/badge/DEFCON%2028-BTV-blue">
    </a><br>
    <a href="https://github.com/quark-engine/quark-engine/actions/workflows/pytest.yml">
        <img alt="build status" src="https://github.com/quark-engine/quark-engine/actions/workflows/pytest.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/quark-engine/quark-engine">
        <img alt="codecov" src="https://codecov.io/gh/quark-engine/quark-engine/branch/master/graph/badge.svg">
    </a>
    <a href="https://github.com/18z/quark-rules/blob/master/LICENSE">
        <img alt="license" src="https://img.shields.io/badge/License-GPLv3-blue.svg">
    </a>
    <a href="https://www.python.org/downloads/release/python-31015/">
        <img alt="python version" src="https://img.shields.io/badge/python-3.10-blue.svg">
    </a>
    <a href="https://pypi.org/project/quark-engine/">
        <img alt="PyPi Download" src="https://pepy.tech/badge/quark-engine">
    </a><br>
    <a href="https://twitter.com/quarkengine">
        <img alt="Twitter" src="https://img.shields.io/twitter/follow/quarkengine?style=social">
    </a><br>
    <img src="https://i.imgur.com/8GwkWei.png"/>
</p>

# New Features Coming Soon to Quark Agent


![Oct-11-2024 17-27-46](https://github.com/user-attachments/assets/6643b80b-bd85-450a-b646-9ef1a8b55bc3)


![Screenshot 2024-09-26 at 2 40 55 PM](https://github.com/user-attachments/assets/9a83b256-1b9f-480f-a061-2400e2e868bc)
<img width="1507" alt="Screenshot 2024-09-26 at 2 41 52 PM" src="https://github.com/user-attachments/assets/b6c3c1bf-aa6a-40e3-aebb-7f1ec375d3d5">

We are currently focused on:

- The next step of the detection process for auto-suggestion.
- Effortlessly create detection workflows with natural language—no coding required.
- Easily adjust and refine workflows through an intuitive drag-and-drop interface.
- Instantly update and integrate changes as Quark Agent understands and adapts to workflow modifications.

We are committed to providing an intuitive and user-friendly experience, enabling users to design detection workflows seamlessly through both textual and visual methods. 

Many features are still under development and fine-tuning, and we will roll them out step by step as they become ready.

If you have any suggestions, please don’t hesitate to share them with us!

To stay updated with the latest news, make sure to watch our GitHub repository and follow us on [X (Twitter)](https://twitter.com/quarkengine).

# Quark Agent - Your AI-powered Android APK Analyst

![quark agent demo](https://hackmd.io/_uploads/By6ggTni0.png)

With Quark Agent, you can perform analyses using only natural language. It creates Quark Script code following your ideas and adjusts the code promptly as you provide feedback.

# Showcase:

Here’s a demonstration of using Quark Agent to detect the CWE-798 vulnerability in the ovaa.apk file.

### Step 1: Environment Requirements

* Make sure your Python version is 3.10 or above.
* Make sure you have the following packages installed:
  + C++ Compiler ([GCC13](https://gcc.gnu.org/)/[Microsoft Visual Studio](https://visualstudio.microsoft.com/))
  + [Cmake](https://cmake.org/)
  + [Git](https://git-scm.com/)
  + [iputils-ping](https://github.com/iputils/iputils/tree/master) (Only required for Linux users)
* Install [Shuriken-Analyzer](https://github.com/Shuriken-Group/Shuriken-Analyzer) by running:
    ```
    pip install git+https://github.com/Fare9/Shuriken-Analyzer.git@main#subdirectory=shuriken/bindings/Python/
    ```

### Step 2: Install Quark Agent

*   Install Quark Agent by running:

```bash
git clone https://github.com/quark-engine/quark-engine.git && cd quark-engine
pip install .[QuarkAgent]
```

### Step 3: Prepare the Detection Rule and the Sample File

```bash
.
├── ...
├── quark                   
    ├── ...           
    ├── agent               # Put rule file and sample file here
    ├── ...                
```

You can download the **rule file** [here](https://github.com/quark-engine/quark-script/blob/main/constructCryptoGraphicKey.json) and the **sample file** [here](https://github.com/oversecured/ovaa).

### Step 4: Add your OpenAI API key

Add your OpenAI API key in `quarkAgentWeb.py`

```python
os.environ["OPENAI_API_KEY"] = 'your-api-key-here'
```

### Step 5: Run Quark Agent

```bash
$ cd quark/agent
$ python3 quarkAgentWeb.py

# You can now chat with Quark Agent in your browser. 
# The default URL is http://127.0.0.1:5000
```

Open a browser and navigate to `127.0.0.1:5000` to start using Quark Agent

See more CWE detections using [quark scripts](https://quark-engine.readthedocs.io/en/latest/quark_script.html) and play them with Quark Agent !

# Acknowledgments

### The Honeynet Project

<a href="https://www.honeynet.org"> <img style="border: 0.2px solid black" width=115 height=150 src="https://i.imgur.com/znu7cMJ.png" alt="Honeynet.org logo"> </a>

### Google Summer Of Code

Quark-Engine has been participating in the GSoC under the Honeynet Project!

*   2021:
    *   [YuShiang Dang](https://twitter.com/YushianhD): [New Rule Generation Technique & Make Quark Everywhere Among Security Open Source Projects](https://quark-engine.github.io/2021/08/17/GSoC-2021-YuShiangDang/)
    *   [Sheng-Feng Lu](https://twitter.com/haeter525): [Replace the core library of Quark-Engine](https://quark-engine.github.io/2021/08/17/GSoC-2021-ShengFengLu/)

Stay tuned for the upcoming GSoC! Join the [Honeynet Slack chat](https://gsoc-slack.honeynet.org/) for more info.

# Core Values of Quark Engine Team

*   We love **battle fields**. We embrace **uncertainties**. We challenge **impossibles**. We **rethink** everything. We change the way people think. And the most important of all, we benefit ourselves by benefit others **first**.
