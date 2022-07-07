import math

def xpblock_to_fafb(z_block,y_block,x_block,z_coo,y_coo,x_coo):
    '''
    函数功能:xp集群上的点到fafb原始坐标的转换
    输入:xp集群点属于的块儿和块内坐标,每个块的大小为1736*1736*26(x,y,z顺序)
    输出:fafb点坐标
    z_block:xp集群点做所在块儿的z轴序号
    y_block:xp集群点做所在块儿的y轴序号
    x_clock:xp集群点做所在块儿的x轴序号
    z_coo:xp集群点所在块内的z轴坐标
    y_coo:xp集群点所在块内的y轴坐标
    x_coo:xp集群点所在块内的x轴坐标
    
    '''
    
    #第一个：这里是我自己按照偏移量算的,block大小用的是 94*2048*2048
    #x_fafb = 1736 * 4 * x_block - 18250 + 4 * x_coo
    #y_fafb = 1736 * 4 * y_block - 19840 + 4 * y_coo
    #z_fafb = 26 * z_block + 1 + z_coo 
    
    #第二个：原来的,z准确的,x,y误差超过5,block大小为 26*1736*1736
    #x_fafb = 1736 * 4 * x_block - 17830 + 4 * x_coo
    x_fafb = 1736 * 4 * x_block - 17631 + 4 * x_coo
    #y_fafb = 1736 * 4 * y_block - 19419 + 4 * y_coo
    y_fafb = 1736 * 4 * y_block - 19211 + 4 * y_coo
    z_fafb = 26 * z_block + 15 + z_coo
    #z_fafb = 26 * z_block + 30 + z_coo
    return ( x_fafb , y_fafb , z_fafb)


def swc_to_xpblock(x,y,z):
    '''
    swc所在的block转化为xp集群原数据位置
    输入:swc坐标,其中swc块大小为522*810*1620(z,y,x顺序)
    输出:xp集群原始数据block位置及块内坐标
    x:swc坐标x
    y:swc坐标y
    z:swc坐标z
    '''
    
    #师姐给的计算方式,只适用于522*810*1620的数据
    #注意:在满足[x1_block,x2_block]之间的坐标[x1_swc,x2_swc]都属于x_block块，z同理
    #注意：因为y方向swc与fafb反方向,所以满足[y2_block,y1_block]的坐标[y1_swc,y2_swc]都属于y2_block块
    x_temp = x / 54 + 6 
    y_temp = 18 - y / 54
    z_temp = 2 * z / 4.0625
    
    x_block = math.floor(x_temp)
    x_coo = math.floor(( x_temp - x_block ) * 1736 )
    z_block = math.floor(z_temp)
    z_coo = math.floor( ( z_temp - z_block ) * 26 )
    y_block = math.ceil(y_temp)
    y_coo = math.ceil(( y_temp - y_block + 1 ) * 1736 ) - 1
    return (z_block,y_block,x_block,z_coo,y_coo,x_coo)
    
def revise_swc():
    f1 = open('E://EE_work//0627gila//all_cluster_add_isolate.swc','r')
    f2 = open('E://EE_work//0627gila //all_cluster_add_isolate_revise.swc',)
    

def main():
    print("hello world!")
    
if __name__ == '__main__':
    #t = xpblock_to_fafb(79,12,28,0,1644,698)
    #t = xp_to_fafb(83,12,29,30,1033,894)
    (t1,t2,t3,t4,t5,t6)=swc_to_xpblock(1427,475,542)
    p=xpblock_to_fafb(t1,t2,t3,t4,t5,t6)
    #p=xpblock_to_fafb(79,12,28,15,1760-156,770-156)
    print(p)