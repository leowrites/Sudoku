import numpy as np
import random
import cell
import subgrid
import os
import time

# figure out how to backtrace

class Sudoku:
    def __init__(self):
        self.number_for_row =[[x for x in range(1, 10)] for x in range(9)]
        self.number_for_column = [[x for x in range(1, 10)] for x in range(9)]
        self.subgrid = self.create_subgrid()
        self.grid = self.create_sudoku()
    
    def create_subgrid(self)->list:
        """Create and return a list of subgrid objects"""
        return [subgrid.Subgrid(i) for i in range(0, 9)]
    
    def create_sudoku(self)->list:
        """Initialize cells by assigning each cell a grid, and return the numpy array"""
        grid = [[None for x in range(9)] for row in range(9)]
        for row in range(0,9):
            for column in range(0,9):
                if row <= 2 and column <=2:
                    grid[row][column] = cell.Cell(0)
                elif row <= 2 and 3 <= column <= 5:
                    grid[row][column] = cell.Cell(1)
                elif row <= 2 and 6 <= column <= 8:
                    grid[row][column] = cell.Cell(2)
                elif 3 <= row <= 5 and column <= 2:
                    grid[row][column] = cell.Cell(3)
                elif 3 <= row <= 5 and 3 <= column <= 5:
                    grid[row][column] = cell.Cell(4)
                elif 3 <= row <= 5 and 6 <= column <= 8:
                    grid[row][column] = cell.Cell(5)
                elif 6 <= row <= 8 and column <= 2:
                    grid[row][column] = cell.Cell(6)
                elif 6 <= row <= 8 and 3 <= column <= 5:
                    grid[row][column] = cell.Cell(7)
                elif 6 <= row <= 8 and 6 <= column <= 8:
                    grid[row][column] = cell.Cell(8)
        return grid

    def generate_sudoku(self):
        """
        generates a new sudoku
        use a while loop
        """

        # randomly generate the first row 
        random_order_number = [x for x in range(1, 10)]
        random.shuffle(random_order_number)
        for x in range(9):
            value = random_order_number[x]
            this_cell = self.grid[0][x]
            this_cell.value = value
            self.remove_value(this_cell, 0, x, value)

        row = 1
        column = 0
        while row <9 and column < 9:
            time.sleep(0.05)
            # search for options
            # should only be done once for each cell
            this_cell = self.grid[row][column]
            if this_cell.options == None:
                this_cell.options = self.find_options(row, column, this_cell.grid)

            if not this_cell.options:
                # backtrace should only happen when there is no options for this cell
                row, column = self.backtrace(this_cell, row, column)

            else:
                # case 3: the number has options and the number returned from the cell is valid
                if this_cell.value != None:
                    self.add_value(this_cell, row, column)
                this_cell.get_value_from_options()
                # when you switch the value for a value from the option, put the current value back into the row
                self.remove_value(this_cell, row, column, this_cell.value)
                if column == 8:
                    row += 1
                    column = 0
                else:
                    column += 1
            try:
                self.print_detail(this_cell, row, column)
            except IndexError:
                pass

    def find_options(self, current_row, current_column, subgrid_number)->list:
        """
        finds the possible options for the current cell
        if no options are found, return to the last cell

        return the options
        """
        row = self.number_for_row
        column = self.number_for_column
        subgrid = self.subgrid[subgrid_number].avaliable_numbers
        options = list(set(row[current_row]) & set(column[current_column]) & set(subgrid))
        options = [x for x in options if x != 0]
        return options

    def backtrace(self, this_cell,  row, column):
            # add the number of this cell back to row, column and grid
        if this_cell.value != None:
            self.add_value(this_cell, row, column)
        this_cell.reset_cell()
        if column == 0:
            row -= 1
            column = 8
        else:
            column -=1
        return row, column
        
    def add_number_back_list(self, target:list, value:int, position:int)->None:
        """when the value of a cell gets deleted, the number gets put back to the array"""
        target[position].append(value)

    def add_number_back_grid(self, target, value):
        self.subgrid[target].add_number(value)
    
    def add_value(self, cell, row, column)->None:
        self.add_number_back_list(self.number_for_row, cell.value, row)
        self.add_number_back_list(self.number_for_column, cell.value, column)
        self.add_number_back_grid(cell.grid, cell.value)

    def remove_value(self, cell:cell.Cell, row:int, column:int, value:int)->None:
        """Removes the value from row, column and grid"""
        self.remove_number_from_list(self.number_for_row, value, row)
        self.remove_number_from_list(self.number_for_column, value, column)
        self.remove_number_from_grid(self.subgrid[cell.grid], value)

    def remove_number_from_list(self, target:list, value:int, position:int)->None:
        """
        when a new cell is given a value, the corresopnding value in the row/column is set to 0
        return an array where the corresopnding position in the target is set to 0
        """
        target[position].remove(value)

    def remove_number_from_grid(self, grid:subgrid.Subgrid, value:int)->None:
        """
        when a new cell is given a value, the corresopnding value in the grid is removed
        to prevent dupliicate values
        """
        grid.remove_number(value)
    
    def clear(self):
        os.system('clear')

    def print_detail(self, cell, row, column):
        self.clear()
        print(np.array([cell.value for row in self.grid for cell in row]).reshape(9,9))
        print(f'number in grid: {self.subgrid[cell.grid].avaliable_numbers}')
        print(f'number in row: {self.number_for_row[row]}')
        print(f'number in column: {self.number_for_column[column]}')
        print(f'options: {cell.options}')

test = Sudoku()
test.generate_sudoku()