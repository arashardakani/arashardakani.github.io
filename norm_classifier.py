import torch

class norm_classifier(torch.autograd.Function):

    @staticmethod
    def forward(ctx, tensor, constant):
        ctx.constant = constant
        ctx.save_for_backward(torch.abs_(tensor/constant) > 1.)
        return torch.clamp(  tensor/constant , -1., 1.).cuda()


    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        return torch.where(input, torch.tensor(0.).cuda(), grad_output ).cuda(), None



Normclass = norm_classifier.apply

