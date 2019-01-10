import deleteman as dm

test = dm.DeleteMan(model_file='file', input_path='./train/inputs', output_path='./train/outputs', valid_path='./validation',size_x=288, size_y=288)
test.run(times=100,epochs=20,batch_size=5)