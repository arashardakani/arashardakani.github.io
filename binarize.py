import torch

class binarize(torch.autograd.Function):

    @staticmethod
    def forward(ctx, tensor, constant):
        
        return torch.sign(tensor).cuda() * torch.where( torch.bernoulli( torch.clamp( torch.abs_(tensor*constant) , 0., 1.)  ) > 0.5 , torch.tensor(constant).cuda() , torch.tensor(-constant).cuda() ).cuda()
        #return torch.where( torch.bernoulli( (torch.clamp( tensor*constant , -1., 1.) + 1.)/2. ) > 0.5 , torch.tensor(1./constant).cuda() , torch.tensor(-1./constant).cuda() ).cuda()
    
    
        #return torch.where( torch.bernoulli( torch.clamp( (tensor/constant+1.)/2 , 0., 1.) ) > 0.5 , torch.tensor(1.).cuda() , torch.tensor(-1.).cuda() ).cuda() 
        #return ( torch.floor( tensor/constant * 1024. )/1024.).cuda()
        #return (tensor/constant ).cuda()
        #return torch.where(  tensor > 0. , torch.tensor(constant * 1.).cuda(), torch.tensor(-1. * constant).cuda()).cuda() 


    @staticmethod
    def backward(ctx, grad_output):
        return grad_output.cuda(), None



Binarize = binarize.apply

