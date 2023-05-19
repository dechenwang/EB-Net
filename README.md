<div align="center">Documentation</div>
train.py    ## train model <br />
test.py    ## val model <br />
predict.py   ## detect model <br />
<br />
ultralytics/models/v8/   ## all train xx.yml

ultralytics/nn/    ## innovation points and comparison codes, such as DSFormer, CroSPPF, MHSA, shuffleattention, aspp, etc.

ultralytics/yolo/utils/    ## metrics.py tal.py and loss.py: DDIou

For the experiments with V3-tiny, v5, v5lite, yolox, and v7-tiny, we use code from yolo air: <br />
If readers do not know how to use air, please contact us.

https://github.com/iscyy/yoloair
-----------------------------------------------------------------------------------------------------------------------------------------------------------
<div align="center">Datasets</div>
<p>
yolo, nanodet and fastestdet formats: <br />
link：https://pan.baidu.com/s/140iXAPbX_SMHMM0EI1E8HA?pwd=e3dz  <br />
extraction code：e3dz  <br />
</p>
-----------------------------------------------------------------------------------------------------------------------------------------------------------
<div align="center">Models</div>
our res models: <br />
link：https://pan.baidu.com/s/11SB4hKQEnbDqHbCRcVTtKQ?pwd=ujgc  <br />
extraction code：ujgc 
<p></p>
-----------------------------------------------------------------------------------------------------------------------------------------------------------
<div align="center">Question</div>
<p>Question 1: How can I view FastestDet's FLOPs? <br />
look eval.py in FastestDet: <br />
origin: stat(model.cpu(), input_size=(3, cfg.input_height, cfg.input_width)) <br />
to: summary(model, input_size=(3, cfg.input_height, cfg.input_width)) <br />
![image](https://github.com/dechenwang/NB-Net/blob/master/fastestdet.png)
<br />
Question 2: How to calculate the Speed of NanoDet? <br />
look demo.py in NanoDet: <br />
![image](https://github.com/dechenwang/NB-Net/blob/master/nano.png)
get three times, the data column processing, into excel, by calculating the average time can get Speed</p>
-----------------------------------------------------------------------------------------------------------------------------------------------------------
<div align="center">Results</div>
codes train results <br />
If readers need ablation experiment weights and comparison experiment weights, please contact us <br />
![image](https://github.com/dechenwang/NB-Net/blob/master/trainres.png) <br />
-----------------------------------------------------------------------------------------------------------------------------------------------------------
