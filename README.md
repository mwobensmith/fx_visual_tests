# fx_visual_tests
Experimental python test suite

Currently Mac and Ubuntu Linux only.
Requires Java SDK 8 (Mac) or 7/8 (Linux). Does not work with Java 9.

    git clone https://github.com/mwobensmith/fx_visual_tests
    cd fx_visual_tests
    cd bootstrap
    ./bootstrap.sh
    virtualenv .
    source bin/activate
    pip install -e .
    fx_visual_tests
