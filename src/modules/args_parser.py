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

from argparse import ArgumentParser


def args_parser():
    arg_parse = ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None,
                           help="path to Video File ")
    arg_parse.add_argument("-i", "--image", default=None,
                           help="path to Image File ")

    args = vars(arg_parse.parse_args())

    return args
