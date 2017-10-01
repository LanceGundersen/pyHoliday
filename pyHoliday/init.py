import yaml

configFilePath = 'config.yml'

with open(configFilePath, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    continuousRun = cfg['setup']['loop']
    sleep = int(float(cfg['setup']['sleep']))
    platform = cfg['setup']['platform']
    # Audio Files
    intro = cfg['alarm']['intro']
    alarm = cfg['alarm']['alarm']
    voice = cfg['alarm']['voice']
