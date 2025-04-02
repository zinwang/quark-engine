+++++++++++++++++++++++
Installing Quark-Engine
+++++++++++++++++++++++

Steps To Install Quark-Engine
-----------------------------

Step 1. Install Shuriken Analyzer Required
===========================================

-  Install packages required for Shuriken Analyzer:
    -  In Debian-based Linux distributions (Debian/Kali/Ubuntu):
        .. code-block::
            $ apt install build-essential g++-13 gcc-13 cmake git iputils-ping
            $ export CC=gcc-13 CXX=g++-13
    -  In MacOS:
        .. code-block::
            $ brew install gcc@13 cmake git
   -  In Windows: Download the following installer for Windows and execute:
        -  `Microsoft Virtual Studio <https://visualstudio.microsoft.com/downloads/>`__
        -  `cmake <https://cmake.org/download/>`__
        -  `git <https://git-scm.com/downloads/win>`__

-  Install Shuriken Analyzer:
    .. code-block::
        pip install git+https://github.com/Fare9/Shuriken-Analyzer.git@main#subdirectory=shuriken/bindings/Python/

Step 2. Install Quark-Engine
=============================

-  From PyPi:
    .. code-block::
        $ pip install -U quark-engine

-  Or you can install from source:
    .. code-block::
        $ git clone https://github.com/quark-engine/quark-engine.git
        $ cd quark-engine/
        $ pipenv install --skip-lock
        $ pipenv shell

Step 3. Check if Quark-Engine is installed
===========================================

Run the help cmd of quark:
.. code-block::
    $ quark --help

Once you see the following message, then you’re all set:

.. code-block::

    Usage: quark [OPTIONS]

      Quark is an Obfuscation-Neglect Android Malware Scoring System

    Options:
      -s, --summary TEXT              Show summary report. Optionally specify the
                                      name of a rule/label
      -d, --detail TEXT               Show detail report. Optionally specify the
                                      name of a rule/label
      -o, --output FILE               Output report in JSON
      -w, --webreport FILE            Generate web report
      -a, --apk FILE                  APK file  [required]
      -r, --rule PATH                 Rules directory  [default:
                                      /home/jensen/.quark-engine/quark-
                                      rules/rules]
      -g, --graph [png|json]          Create call graph to call_graph_image
                                      directory
      -c, --classification            Show rules classification
      -t, --threshold [100|80|60|40|20]
                                      Set the lower limit of the confidence
                                      threshold
      -i, --list [all|native|custom]  List classes, methods and descriptors
      -p, --permission                List Android permissions
      -l, --label [max|detailed]      Show report based on label of rules
      -C, --comparison                Behaviors comparison based on max confidence
                                      of rule labels
      --generate-rule DIRECTORY       Generate rules and output to given directory
      --core-library [androguard|rizin|radare2|shuriken]
                                      Specify the core library used to analyze an
                                      APK
      --multi-process INTEGER RANGE   Allow analyzing APK with N processes, where
                                      N doesn't exceeds the number of usable CPUs
                                      - 1 to avoid memory exhaustion.  [x>=1]
      --version                       Show the version and exit.
      --help                          Show this message and exit.


To learn how to scan multiple samples in a directory, please have a look at :ref:`Directory Scanning <dir_scan>`
