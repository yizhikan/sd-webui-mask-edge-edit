import modules.scripts as scripts
import gradio as gr
import numpy as np
from PIL import Image
import cv2
from modules.processing import process_images


def edgeEdit(src_grey, src_original, kernalsizesmall=10, kernalsizebig=30, kernald=20, reversal=True):
    # outputType="dAndBig":内膨胀外腐蚀    outputType="smallAndBig":内小腐蚀外大腐蚀
    # outputType="d":返回外圈白色膨胀结果    outputType="small":返回外圈白色腐蚀结果
    # 按照"d" "small" "dAndBig" "smallAndBig" 顺序返回结果
    resMaskImage = []
    resOriginal = []
    # 读取图片

    img = cv2.cvtColor(np.asarray(src_grey),  cv2.COLOR_RGB2BGR)
    if reversal==False:
        resOriginalImageMask = img
        img = ~img

    src = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 通过单阈值获得二值图像
    ret, src = cv2.threshold(src, 102, 255, cv2.THRESH_BINARY)

    # 设置卷积核
    kernelsmall = np.ones((kernalsizesmall, kernalsizesmall), np.uint8)  # 0是黑色，255是白色
    kernelbig = np.ones((kernalsizebig, kernalsizebig), np.uint8)  # 0是黑色，255是白色
    kernelD = np.ones((kernald, kernald), np.uint8)  # 0是黑色，255是白色

    source = cv2.cvtColor(np.asarray(src_original),  cv2.COLOR_RGB2BGR)

    #未经处理的图
    resOriginalImage = cv2.add(source, np.zeros(np.shape(source), dtype=np.uint8), mask=src)

    # 图像膨胀处理
    resDMask = cv2.dilate(src, kernelD)
    #下面是预览图
    resD = cv2.add(source, np.zeros(np.shape(source), dtype=np.uint8), mask=resDMask)

    # 图像腐蚀处理(小)
    resSamllMask = cv2.erode(src, kernelsmall)  # 注意膨胀和腐蚀都是对白色255来说的，
    resSmall = cv2.add(source, np.zeros(np.shape(source), dtype=np.uint8), mask=resSamllMask)

    # 图像腐蚀处理(大)
    resBigMask = cv2.erode(src, kernelbig)  # 注意膨胀和腐蚀都是对白色255来说的，


    resBigMask = ~resBigMask
    resSmallAndBigMask = cv2.add(resSamllMask, np.zeros(np.shape(resSamllMask), dtype=np.uint8), mask=resBigMask)
    resSmallAndBig = cv2.add(source, np.zeros(np.shape(source), dtype=np.uint8), mask=resSmallAndBigMask)

    resDAndBigMask = cv2.add(resDMask, np.zeros(np.shape(resDMask), dtype=np.uint8), mask=resBigMask)
    resDAndBig = cv2.add(source, np.zeros(np.shape(source), dtype=np.uint8), mask=resDAndBigMask)


    # original
    resMaskImage.append(Image.fromarray(cv2.cvtColor(resOriginalImageMask, cv2.COLOR_BGR2RGB)))
    resOriginal.append(Image.fromarray(cv2.cvtColor(resOriginalImage, cv2.COLOR_BGR2RGB)))
    # d
    resDMask=~resDMask
    resMaskImage.append(Image.fromarray(cv2.cvtColor(resDMask, cv2.COLOR_BGR2RGB)))
    resOriginal.append(Image.fromarray(cv2.cvtColor(resD, cv2.COLOR_BGR2RGB)))
    # small
    resSamllMask=~resSamllMask
    resMaskImage.append(Image.fromarray(cv2.cvtColor(resSamllMask, cv2.COLOR_BGR2RGB)))
    resOriginal.append(Image.fromarray(cv2.cvtColor(resSmall, cv2.COLOR_BGR2RGB)))
    # dAndBig
    resMaskImage.append(Image.fromarray(cv2.cvtColor(resDAndBigMask, cv2.COLOR_BGR2RGB)))
    resOriginal.append(Image.fromarray(cv2.cvtColor(resSmallAndBig, cv2.COLOR_BGR2RGB)))
    # smallAndBig
    resMaskImage.append(Image.fromarray(cv2.cvtColor(resSmallAndBigMask, cv2.COLOR_BGR2RGB)))
    resOriginal.append(Image.fromarray(cv2.cvtColor(resDAndBig, cv2.COLOR_BGR2RGB)))

    return resMaskImage + resOriginal



class ExtensionTemplateScript(scripts.Script):
    # Extension title in menu UI
    def title(self):
        return "Mask Edge Edit"

    # Decide to show menu in txt2img or img2img
    # - in "txt2img" -> is_img2img is `False`
    # - in "img2img" -> is_img2img is `True`
    #
    # below code always show extension menu
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    # Setup menu ui detail
    def ui(self, is_img2img):
        with gr.Accordion('Mask Edge Edit', open=False):
            with gr.Column():
                gr.HTML(value="<p>ATTENTION: Please check your mask image!!! Make sure the mask image is the same size as the original image</p>", label="Positive points")
                gr.HTML(value="<p>If your mask image is normal, the area in the mask image you want to inpaint is white while other area is black, so you don't need to tick the 'Tick it if black mask' box. Otherwise, you need to tick it.</p>", label="Positive points")
                input_image_grey = gr.Image(label="Mask Image",
                    show_label=True, source="upload", type="pil", image_mode="RGB")
                input_image_original = gr.Image(label="Original Image",
                    show_label=True, source="upload", type="pil",
                    image_mode="RGB")
                gr.HTML(
                    value="<p>First row: Original mask image AND Result of add Original image with the NEGATED mask</p>",
                    label="Positive points")
                gr.HTML(
                    value="<p>Second row: Shrunken mask image AND Result of add Original image with the NEGATED mask {Controled by 'Shrink the mask area'}</p>",
                    label="Positive points")
                gr.HTML(
                    value="<p>Third row: Expanded mask image AND Result of add Original image with the NEGATED mask {Controled by 'Expand mask area(small)'}</p>",
                    label="Positive points")
                gr.HTML(
                    value="<p>Fourth row: Edge mask image between larger expanded mask {Controled by 'Expand mask area(big)'} and expanded mask {Controled by 'Expand mask area(small)'} AND Result of add Original image with the mask</p>",
                    label="Positive points")
                gr.HTML(
                    value="<p>Fifth row: Edge mask image between Shrunken mask {Controled by 'Shrink the mask area'} and larger expanded mask {Controled by 'Expand mask area(big)'} AND Result of add Original image with the mask</p>",
                    label="Positive points")
                mask_image = gr.Gallery(
                     label='Edge edit Output', show_label=True).style(grid=5)
                gr.HTML(
                    value="<p>ATTENTION: Make sure 'Expand mask area(big)' is larger than 'Expand mask area(small)'</p>",
                    label="Positive points")
                with gr.Row():
                    strengthOfMaskSmall = gr.Slider(
                        minimum=0.0,
                        maximum=100.0,
                        step=1,
                        value=0,
                        label="Shrink the mask area"
                    )
                    strengthOfMaskLarge1 = gr.Slider(
                        minimum=0.0,
                        maximum=100.0,
                        step=1,
                        value=0,
                        label="Expand mask area(small)"
                    )
                    strengthOfMaskLarge2 = gr.Slider(
                        minimum=0.0,
                        maximum=100.0,
                        step=1,
                        value=0,
                        label="Expand mask area(big)"
                    )

                    Checkbox = gr.Checkbox(
                         False,
                         label="Tick it if black mask"
                    )
                with gr.Row():
                    run_button = gr.Button(value="Preview mask edit")

            run_button.click(
                fn=edgeEdit,
                inputs=[input_image_grey, input_image_original,
                    strengthOfMaskLarge1, strengthOfMaskLarge2,
                    strengthOfMaskSmall,Checkbox],
                outputs=[mask_image],
                show_progress=False)

        # TODO: add more UI components (cf. https://gradio.app/docs/#components)
        return [input_image_grey, input_image_original, strengthOfMaskSmall,
            strengthOfMaskLarge1, strengthOfMaskLarge2, Checkbox, mask_image]

        # Extension main process
        # Type: (StableDiffusionProcessing, List<UI>) -> (Processed)
        # args is [StableDiffusionProcessing, UI1, UI2, ...]
    def run(self, p, angle, checkbox):
        # TODO: get UI info through UI object angle, checkbox
        proc = process_images(p)
        # TODO: add image edit process via Processed object proc
        return proc

