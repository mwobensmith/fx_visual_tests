# fx_visual_tests
Experimental python test suite

Supports Mac, Ubuntu Linux and Windows.

Requires Java SDK 8 (Mac) or 7/8 (Linux). Does not work with Java 9.

Mac instructions:

    git clone https://github.com/mwobensmith/fx_visual_tests
    cd fx_visual_tests
    virtualenv .
    source bin/activate
    pip install -e .
    fx_visual_tests

Ubuntu Linux instructions:

    git clone https://github.com/mwobensmith/fx_visual_tests
    cd fx_visual_tests
    cd bootstrap
    ./bootstrap.sh
    cd ..
    virtualenv .
    source bin/activate
    pip install -e .
    fx_visual_tests
    
Windows instructions:

Install Python 2.7

Add the following paths to your system environment variable for PATH:

c:\Python27;c:\Python27\Scripts

Run the following commands:

    git clone https://github.com/mwobensmith/fx_visual_tests
    cd fx_visual_tests
    virtualenv .
    Scripts\activate
    pip install -e .
    fx_visual_tests
    
Note that you will get a fatal error from Sikuli, regarding a path issue. This is expected. Log out and back in to your Windows account (or restart) and repeat just the following commands:

    cd fx_visual_tests
    virtualenv .
    Scripts\activate
    pip install -e .
    fx_visual_tests
    
