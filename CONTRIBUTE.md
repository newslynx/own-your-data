To populate the vendor directory, run

    mkdir vendor
    mkdir vendor/packages
    cat downloads.txt | wget

To add a python package to the list, just add it to requirements.txt. When preparing the vendor directory for distribution, we can then run: 

    pip install -d vendor/packages -r requirements.txt

To create a newer Vagrant box

    cd vendor
    vagrant up
    vagrant package
    rm vendor/own-your-data.box
    mv package.box vendor/own-your-data.box
