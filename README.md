# sd-webui-mask-edge-edit

A stable-diffusion-webui extension for edit your mask edge

To solve the problem that the masked area cannot perfectly cover the target

The mask image may be the predict result of Segment Anything Model, or other popular segment models.

# Why this project
## First Problem

When I use Segment Anything Model to make mask image for my image, as you see the target is the girl.

Original Image

<img src="https://user-images.githubusercontent.com/56151705/231697127-edcc1027-265a-4abe-8d6b-0da5b9706a1d.jpg"  width="400"/>

Mask Image

<img src="https://user-images.githubusercontent.com/56151705/231692685-029cba73-8160-4dca-9ce6-6afaa33c7890.png"  width="400"/>

Then I add the mask with the original image, I find that the masked area cannot perfectly cover the target area. Some red pixels still remain near the skirt. 

<img src="https://user-images.githubusercontent.com/56151705/231693213-065e26e2-91be-49e0-8fc6-1a3924430972.png"  width="400"/>

The problem will exit even in the generate image

<img src="https://user-images.githubusercontent.com/56151705/231697683-d527838d-fc0e-4d6e-b26a-45d9e06d0573.png"  width="400"/>

So I think that will be a good choice to expand the mask area, which allows me to inpaint the girl

## Second Problem

This problem comes from the solution of the first problem

After I inpaint the image with the expanded mask, I found some edge blemishes appearing on the image that would make it appear that it is generated

Look at the following generate image. It may be nice if you don't check any detail in the image. Of course, it solve the first problem.

<img src="https://user-images.githubusercontent.com/56151705/231698520-00bacb87-4568-457f-99ad-50d357354cf3.png"  width="400"/>

