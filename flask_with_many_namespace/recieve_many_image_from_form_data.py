import io as io_orin
from flask import Blueprint, Response, request
from flask_restx import Api, Resource
import cv2
import numpy as np


blueprint = Blueprint("identities", __name__)
ns = Api(blueprint)
namespace = ns.namespace("identities")


@namespace.route("/group_image", methods=["GET", "POST"])
class FindAll(Resource):
    # @auth.login_required
    def post(self):
        """
        Group the same faces in list image.
        Returns: json data
        """
        # get data
        files = request.files
        files = list(files.listvalues())
        if len(files[0]) > 1:
            files = files[0]
        list_img_array = []
        for file in files:
            if isinstance(file, list):
                file = file[0]
            in_memory_file = io_orin.BytesIO()
            file.save(in_memory_file)
            data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            color_image_flag = 1
            img_array = cv2.imdecode(data, color_image_flag)
            list_img_array.append(img_array)
        print("list_img_array", list_img_array)

        return "OK"
