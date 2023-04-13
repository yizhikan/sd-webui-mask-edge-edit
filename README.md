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

But when you check the details near the mask edge, you will find something wrong. Around the edge, area inside the mask is clean however outsides is dusty.

<img src="https://user-images.githubusercontent.com/56151705/231700658-f8035312-70c7-4d13-9db4-6353f9da4f53.png"  width="400"/>

You can see the same phenomenon near the skirt edge.

After Mask Edge Editting, actually it is inpainting secondly, you will find the quality of edges become better. Like this

<img src="https://user-images.githubusercontent.com/56151705/231702341-ffb8f2b0-71ec-4362-9d6e-0fff0611d0d5.png"  width="400"/>

Zoom it

<img src="https://user-images.githubusercontent.com/56151705/231702983-6add26bf-40a5-446b-b010-2cf2174cf42e.png"  width="400"/>

Comparison: Before edge edit  VS  After edge edit

<img src="https://user-images.githubusercontent.com/56151705/231705016-19ffd460-8146-4d56-a5c9-9e9d8c9731f5.png"  width="800"/>

# How to use

Step 1: Clone to your ./stable-diffusion-webui/extensions

Step 2: You can use it in 'txt2img' or 'img2img'


