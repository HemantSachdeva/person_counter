"""
 Copyright (C) 2022 Hemant Sachdeva <hemant.evolver@gmail.com>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """

from modules.detect_by_image_path import detect_by_image_path
from modules.detect_by_video_path import detect_by_video_path


def human_detector(args):
    image_path = args["image"]
    video_path = args['video']

    writer = None
    if video_path is not None:
        print('[INFO] Opening Video from path.')
        print('[INFO] Press q to close window.')
        detect_by_video_path(video_path, writer)

    elif image_path is not None:
        print('[INFO] Opening Image from path.')
        print('[INFO] Press q to close window.')
        detect_by_image_path(image_path)
