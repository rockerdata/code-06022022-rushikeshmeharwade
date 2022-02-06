rm -r dist ;
python setup.py sdist bdist_wheel ;
if twine check dist/* ; then
    twine upload dist/* ;
fi