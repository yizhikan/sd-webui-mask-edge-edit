# sd-webui-mask-edge-edit

A stable-diffusion-webui extension for edit your mask edge

To solve the problem that the masked area cannot perfectly cover the target

The mask image may be the predict result of Segment Anything Model, or other popular segment models.

# Why this project

When I use Segment Anything Model to make mask image for my image, as you see the target is the girl, then I add the mask with the original image, I find that the masked area cannot perfectly cover the target area. Some red pixels still remain near the skirt. 

So I think that will be a good choice to expand the mask area, which allows me to inpaint the girl
