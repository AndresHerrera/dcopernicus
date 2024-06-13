# DCopernicus

Simple Demo of Copernicus Marine Service Toolbox ( Python API ) - copernicusmarine 

## CREATE ENV

```console 
conda create -n copernicus python=3.12
conda activate copernicus
```

## INSTALL DEPENDENCIES

```console 
$ python -m pip install copernicusmarine
$ python -m pip install xarray rasterio
$ python -m pip install rioxarray
$ python -m pip install python-dotenv
```
## CONFIGURE
```console
$ vim .env
```
## RUN 

```console
$ python demoCHL.py
```

```console
$ python demoSPM.py
```

```console
$ python demoUO_VO.py
```