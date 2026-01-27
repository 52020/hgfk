# CI-FLAG-NOT-COMPILE

import argparse


def str2bool(v):
    return v.lower() in ("true", "t", "1")


def init_args():
    parser = argparse.ArgumentParser()
    # params for prediction engine
    parser.add_argument("--use_gpu", type=str2bool, default=False)
    parser.add_argument("--use_xpu", type=str2bool, default=False)
    parser.add_argument("--ir_optim", type=str2bool, default=True)
    parser.add_argument("--use_tensorrt", type=str2bool, default=False)
    parser.add_argument("--min_subgraph_size", type=int, default=15)
    parser.add_argument("--shape_info_filename", type=str, default=None)
    parser.add_argument("--precision", type=str, default="fp32")
    parser.add_argument("--gpu_mem", type=int, default=500)

    # params for text detector
    parser.add_argument("--image_dir", type=str)

    # params for text recognizer
    parser.add_argument("--rec_algorithm", type=str, default='SVTR_LCNet')
    parser.add_argument("--rec_model_dir", type=str, default='../models/221108-svtr.onnx')
    parser.add_argument("--rec_image_shape", type=str, default="3, 32, 320")
    parser.add_argument("--rec_batch_num", type=int, default=6)
    parser.add_argument("--max_text_length", type=int, default=25)
    parser.add_argument(
        "--rec_char_dict_path",
        type=str,
        default="char_std_5990.txt")
    parser.add_argument("--use_space_char", type=str2bool, default=True)
    parser.add_argument(
        "--vis_font_path", type=str, default="./doc/fonts/simfang.ttf")
    parser.add_argument("--drop_score", type=float, default=0.5)

    # output
    parser.add_argument(
        "--draw_img_save_dir", type=str, default="./inference_results")
    parser.add_argument("--save_crop_res", type=str2bool, default=False)
    parser.add_argument("--crop_res_save_dir", type=str, default="./output")

    # multi-process
    parser.add_argument("--use_mp", type=str2bool, default=False)
    parser.add_argument("--total_process_num", type=int, default=1)
    parser.add_argument("--process_id", type=int, default=0)

    parser.add_argument("--benchmark", type=str2bool, default=False)
    parser.add_argument("--save_log_path", type=str, default="./log_output/")

    parser.add_argument("--show_log", type=str2bool, default=True)
    parser.add_argument("--use_onnx", type=str2bool, default=True)
    return parser


class Args:
    use_gpu = False
    use_xpu = False
    ir_optim = True
    use_tensorrt = False
    min_subgraph_size = 15
    shape_info_filename = None
    precision = "fp32"
    gpu_mem = 500

    image_dir = None

    rec_algorithm = "SVTR_LCNet"
    rec_model_dir = None
    rec_image_shape = "3, 32, 320"
    rec_batch_num = 6
    max_text_length = 25
    rec_char_dict_path = None
    use_space_char = True
    vis_font_path = "./doc/fonts/simfang.ttf"
    drop_score = 0.5

    draw_img_save_dir = "./inference_results"
    save_crop_res = False
    crop_res_save_dir = "./output"

    use_mp = False
    total_process_num = 1
    process_id = 0

    benchmark = False
    save_log_path = "./log_output/"

    show_log = True
    use_onnx = True


def parse_args():
    return Args
