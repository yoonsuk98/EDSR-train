import os
from data import srdata
from data import mscoco

class test2014(mscoco.mscoco):
    def __init__(self, args, name='', train=True, benchmark=False):
        # self.q_factor = int(name.replace('DIV2K-Q', ''))
        super(test2014, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )

    def _set_filesystem(self, dir_data):
        self.apath = os.path.join(dir_data, 'mscoco')
        self.dir_hr = os.path.join(self.apath, 'test2014')
        self.dir_lr = os.path.join(self.apath, 'down_test2014')
        if self.input_large: self.dir_lr += 'L'
        self.ext = ('.jpg', '.jpg')

