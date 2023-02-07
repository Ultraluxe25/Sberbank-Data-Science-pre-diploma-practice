I got a problem: after I printed

```bash
conda activate sber2
pip freeze > modules.txt
```

I received file modules.txt which contained such data:

```txt
asttokens @ file:///opt/conda/conda-bld/asttokens_1646925590279/work
backcall @ file:///home/ktietz/src/ci/backcall_1611930011877/work
Bottleneck @ file:///C:/Windows/Temp/abs_3198ca53-903d-42fd-87b4-03e6d03a8381yfwsuve8/croots/recipe/bottleneck_1657175565403/work
certifi @ file:///C:/b/abs_85o_6fm0se/croot/certifi_1671487778835/work/certifi
colorama @ file:///C:/b/abs_a9ozq0l032/croot/colorama_1672387194846/work
comm @ file:///C:/b/abs_1419earm7u/croot/comm_1671231131638/work
contourpy @ file:///C:/b/abs_d5rpy288vc/croots/recipe/contourpy_1663827418189/work
cycler @ file:///tmp/build/80754af9/cycler_1637851556182/work
debugpy @ file:///C:/ci_310/debugpy_1642079916595/work
decorator @ file:///opt/conda/conda-bld/decorator_1643638310831/work
entrypoints @ file:///C:/ci/entrypoints_1649926676279/work
executing @ file:///opt/conda/conda-bld/executing_1646925071911/work
fonttools==4.25.0
ipykernel @ file:///C:/b/abs_b4f07tbsyd/croot/ipykernel_1672767104060/work
ipython @ file:///C:/b/abs_d4_i9p0_36/croot/ipython_1674681439495/work
jedi @ file:///C:/ci/jedi_1644315428305/work
jupyter_client @ file:///C:/b/abs_b9pns5mx5p/croot/jupyter_client_1671703062216/work
jupyter_core @ file:///C:/b/abs_84df679bho/croot/jupyter_core_1672332237650/work
kiwisolver @ file:///C:/b/abs_88mdhvtahm/croot/kiwisolver_1672387921783/work
matplotlib @ file:///C:/b/abs_03z_dj2gty/croot/matplotlib-suite_1670466145509/work
matplotlib-inline @ file:///C:/ci/matplotlib-inline_1661934094726/work
mkl-fft==1.3.1
mkl-random @ file:///C:/ci_310/mkl_random_1643050563308/work
mkl-service==2.4.0
munkres==1.1.4
nest-asyncio @ file:///C:/b/abs_3a_4jsjlqu/croot/nest-asyncio_1672387322800/work
numexpr @ file:///C:/b/abs_a7kbak88hk/croot/numexpr_1668713882979/work
numpy @ file:///C:/b/abs_datssh7cer/croot/numpy_and_numpy_base_1672336199388/work
packaging @ file:///C:/b/abs_cfsup8ur87/croot/packaging_1671697442297/work
pandas @ file:///C:/b/abs_c6fuezktfm/croot/pandas_1670425103552/work
parso @ file:///opt/conda/conda-bld/parso_1641458642106/work
pickleshare @ file:///tmp/build/80754af9/pickleshare_1606932040724/work
Pillow==9.3.0
platformdirs @ file:///C:/b/abs_73cc5cz_1u/croots/recipe/platformdirs_1662711386458/work
ply==3.11
prompt-toolkit @ file:///C:/b/abs_6coz5_9f2s/croot/prompt-toolkit_1672387908312/work
psutil @ file:///C:/Windows/Temp/abs_b2c2fd7f-9fd5-4756-95ea-8aed74d0039flsd9qufz/croots/recipe/psutil_1656431277748/work
pure-eval @ file:///opt/conda/conda-bld/pure_eval_1646925070566/work
Pygments @ file:///opt/conda/conda-bld/pygments_1644249106324/work
pyparsing @ file:///C:/Users/BUILDE~1/AppData/Local/Temp/abs_7f_7lba6rl/croots/recipe/pyparsing_1661452540662/work
PyQt5==5.15.7
PyQt5-sip @ file:///C:/Windows/Temp/abs_d7gmd2jg8i/croots/recipe/pyqt-split_1659273064801/work/pyqt_sip
python-dateutil @ file:///tmp/build/80754af9/python-dateutil_1626374649649/work
pytz @ file:///C:/b/abs_22fofvpn1x/croot/pytz_1671698059864/work
pywin32==305.1
pyzmq @ file///C:/ci/pyzmq_1657616000714/work
sip @ file:///C:/Windows/Temp/abs_b8fxd17m2u/croots/recipe/sip_1659012372737/work
six @ file:///tmp/build/80754af9/six_1644875935023/work
stack-data @ file:///opt/conda/conda-bld/stack_data_1646927590127/work
toml @ file:///tmp/build/80754af9/toml_1616166611790/work
tornado @ file:///C:/ci/tornado_1662476985533/work
traitlets @ file:///C:/b/abs_e5m_xjjl94/croot/traitlets_1671143896266/work
wcwidth @ file:///Users/ktietz/demo/mc3/conda-bld/wcwidth_1629357192024/work
wincertstore==0.2
```

To solve my problem I used clean_librarian_versions function and it gave me another file
requirements.txt with context:

```text
asttokens
backcall
Bottleneck
certifi
colorama
comm
contourpy
cycler
debugpy
decorator
entrypoints
executing
fonttools==4.25.0
ipykernel
ipython
jedi
jupyter_client
jupyter_core
kiwisolver
matplotlib
matplotlib-inline
mkl-fft==1.3.1
mkl-random
mkl-service==2.4.0
munkres==1.1.4
nest-asyncio
numexpr
numpy
packaging
pandas
parso
pickleshare
Pillow==9.3.0
platformdirs
ply==3.11
prompt-toolkit
psutil
pure-eval
Pygments
pyparsing
PyQt5==5.15.7
PyQt5-sip
python-dateutil
pytz
pywin32==305.1
pyzmq
sip
six
stack-data
toml
tornado
traitlets
wcwidth
wincertstore==0.2
```

After I used command 
```bash
pip install -r requirements.txt
```





