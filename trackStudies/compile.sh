rm trackStudy
#g++ -I $PWD $(root-config --cflags --libs) $($PWD/../../../../fastjet-install/bin/fastjet-config --cxxflags --libs --plugins) -fopenmp -O3 -lm -lgomp -o jetAlgoComp jetAlgoComp.cc  -g
g++ -I $PWD $(root-config --cflags --libs) $($PWD/../../../fastjet-install/bin/fastjet-config --cxxflags --libs --plugins) -fopenmp -O3 -lm -lgomp -o trackStudy trackStudies.cc  -g
