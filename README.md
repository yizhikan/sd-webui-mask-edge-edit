# sd-webui-mask-edge-edit

A stable-diffusion-webui extension for edit your mask edge

To solve the problem that the masked area cannot perfectly cover the target

The mask image may be the predict result of Segment Anything Model, or other popular segment models.

# Why this project
## First Problem

When I use Segment Anything Model to make mask image for my image, as you see the target is the girl.

Original Image (img1)

<img src="https://user-images.githubusercontent.com/56151705/231697127-edcc1027-265a-4abe-8d6b-0da5b9706a1d.jpg"  width="400"/>

Mask Image (img2)

<img src="https://user-images.githubusercontent.com/56151705/231692685-029cba73-8160-4dca-9ce6-6afaa33c7890.png"  width="400"/>

Then I add the mask with the original image, I find that the masked area cannot perfectly cover the target area. Some red pixels still remain near the skirt.  (img3)

<img src="https://user-images.githubusercontent.com/56151705/231693213-065e26e2-91be-49e0-8fc6-1a3924430972.png"  width="400"/>

The problem will exist even in the generate image. (img4)

<img src="https://user-images.githubusercontent.com/56151705/231697683-d527838d-fc0e-4d6e-b26a-45d9e06d0573.png"  width="400"/>

So I think that it will be a good choice to expand the mask area, which allows me to inpaint the girl

## Second Problem

This problem comes from the solution of the first problem

After I inpaint the image with the expanded mask, I found some edge blemishes appearing on the image that would make it appear that it is generated

Look at the following generate image. It may be nice if you don't check any detail in the image. Of course, it solve the first problem. (img5)

<img src="https://user-images.githubusercontent.com/56151705/231698520-00bacb87-4568-457f-99ad-50d357354cf3.png"  width="400"/>

But when you check the details near the mask edge, you will find something wrong. Around the edge, area inside the mask is clean however outsides is dusty. (img6)

<img src="https://user-images.githubusercontent.com/56151705/231700658-f8035312-70c7-4d13-9db4-6353f9da4f53.png"  width="400"/>

You can see the same phenomenon near the skirt edge.

After Mask Edge Editting, actually it is second inpainting, you will find the quality of edges become better. Like this (img7)

<img src="https://user-images.githubusercontent.com/56151705/231702341-ffb8f2b0-71ec-4362-9d6e-0fff0611d0d5.png"  width="400"/>

Zoom it (img8)

<img src="https://user-images.githubusercontent.com/56151705/231702983-6add26bf-40a5-446b-b010-2cf2174cf42e.png"  width="400"/>

Comparison: Before edge edit  VS  After edge edit (img10)

<img src="https://user-images.githubusercontent.com/56151705/231705016-19ffd460-8146-4d56-a5c9-9e9d8c9731f5.png"  width="800"/>

# How to use

Step 1: Clone to your ./stable-diffusion-webui/extensions

Step 2: You can use it in 'txt2img' or 'img2img' (img11)

<img src="https://user-images.githubusercontent.com/56151705/231714538-21118ce3-c7a3-431d-bef6-6434bc3ff857.PNG"  width="400"/>

Step 3: Put your mask image (it comes from the predict result of segment model) and original image, Like this (img12)

<img src="https://user-images.githubusercontent.com/56151705/231716232-7c47a12a-f12c-437e-950c-ddca54509925.PNG"  width="400"/>

Step 4: Choose suitable parameter for your first inpaint!

The goal of your first inpaint is to make sure the mask can perfectly cover the object instead of keeping any object pixel remain.

In my example, the original mask is not perfect cover, as you see, in first row, they are original mask and original image. I need to expand the mask image, so I need to set the 'Expand mask area(small)' to 15, then click the 'Preview mask edit' botton. You may need to try several times to make sure the expanded mask can cover it while it can't be expanded too much. By the way, the original image here is 1024 * 1024, check it seriously.  (img13)

<img src="https://user-images.githubusercontent.com/56151705/231718706-f5503522-dc20-4ab7-bfa2-fd219a9cb100.PNG"  width="400"/>

Now the third row is what I need. Use the mask which is from the third row to inpaint. The result of inpainting is img5 (see line.40). This is my inpaint details. (img14) 

!!!!ATTENTION: Denoising strength is 0.95. Mask blur is 4. That is different from Step 5 !!!!

<img src="https://user-images.githubusercontent.com/56151705/231730351-686cfdcc-e73a-41b7-8c17-2edd0f820b4b.png"  width="800"/>

Maybe your mask is overlarge, set the 'Shrink the mask area' to suitable value, then click the 'Preview mask edit' botton. The second row is what you need(see img13).

The meaning of each row of images see below.(img15) It is very detailed

<img src="https://user-images.githubusercontent.com/56151705/231725526-5164fb23-5327-4a2d-9428-aea9e56984bc.PNG"  width="800"/>

Step 5: Make your edge mask. Choose suitable values for 'Shrink the mask area' and 'Expand mask area(big)', and then click the 'Preview mask edit' bottom, you can get the edge mask in the fifth row.  (img16)

<img src="https://user-images.githubusercontent.com/56151705/231732169-a53c874c-061f-4b73-83d5-e287b66e358f.PNG"  width="400"/>

!!!!ATTENTION: 'Shrink the mask area' and 'Expand mask area(big)' cannot be set too large or too small!!!!

TOO SMALL: cannot solve problem 2   TOO LARGE: it will generate other things. You can try it

This is my second inpaint details. (img17) 

!!!!ATTENTION: Denoising strength is 0.4. Mask blur is 20. That is different from Step 4 !!!!

!!!!ATTENTION: What you second inpaint is your first inpaint result !!!!

<img src="https://user-images.githubusercontent.com/56151705/231735689-bd85fc06-9593-4632-b6e1-d9fbd442a50c.png"  width="400"/>


## Ref.
- [continue-revolution/sd-webui-segment-anything](https://github.com/continue-revolution/sd-webui-segment-anything)
- [udon-universe/stable-diffusion-webui-extension-templates](https://github.com/udon-universe/stable-diffusion-webui-extension-templates)
- [Developing extensions · AUTOMATIC1111/stable-diffusion-webui Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Developing-extensions)



