#!/usr/bin/python3
"""
LockBoxes
"""

def canUnlockAll(boxes):
        """
        A method that determines if all the boxes can be opened.

        You have n number of locked boxes in front of you. 
        Each box is numbered sequentially from 0 to n - 1.
        Each box may contain keys to the other boxes.


        - boxes is a list of lists
        - A key with the same number as a box opens that box
        - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
        - The first box boxes[0] is unlocked
        - Return True if all boxes can be opened, else return False
        """
        if not boxes:
                return False
		
        opened_boxes = {0}

        boxes_to_check = [0]

        while boxes_to_check:
                current_box = boxes_to_check.pop()

                for key in boxes[current_box]:
                        if key < len(boxes) and key not in opened_boxes:
                                opened_boxes.add(key)
                                boxes_to_check.append(key)

        return len(opened_boxes) == len(boxes)
