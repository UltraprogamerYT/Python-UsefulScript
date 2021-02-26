from tqdm import tqdm
loop = tqdm(total= 50000, position= 0, leave= False)
for k in range(50000):
	loop.set_description("Loading ".format(k))
	loop.update(1)
loop.close