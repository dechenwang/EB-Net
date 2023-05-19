## <div align="center">Documentation</div>
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
-------------------------------
## <div align="center">Question</div>
Question 1: How can I view FastestDet's FLOPs? <br />
look eval.py in FastestDet: <br />
origin: stat(model.cpu(), input_size=(3, cfg.input_height, cfg.input_width)) <br />
to: summary(model, input_size=(3, cfg.input_height, cfg.input_width)) <br />
![image](https://github.com/dechenwang/NB-Net/assets/104114673/556f5d7d-ec55-4d48-948a-ae163f8686f5)
<br />
Question 2: How to calculate the Speed of NanoDet? <br />
look demo.py in NanoDet: <br />
![image](https://github.com/dechenwang/NB-Net/assets/104114673/4b421b85-2d39-4159-949d-05abaf2f5dc5)
get three times, the data column processing, into excel, by calculating the average time can get Speed
-------------------------------
## <div align="center">Results</div>
codes train results
![image](https://github.com/dechenwang/NB-Net/assets/104114673/f8dded7f-49d0-48e8-a7bc-aa1dc4cb8ee5)
-------------------------------
