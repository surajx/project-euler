def process_grid_data(raw_grid_data):
  row_string_list = raw_grid_data.split('x')
  grid = []
  for row in row_string_list:
    row_int_list = []
    for val in row.split(' '):
      row_int_list.append(int(val))
    grid.append(row_int_list)
  return grid

def get_all_quad_pos(cur_grid_pos, grid_x, grid_y):
  #right
  quad_list = []
  if cur_grid_pos[0]+3 <= grid_x:
    quad_list.append((cur_grid_pos,
            [cur_grid_pos[0]+1,cur_grid_pos[1]],
            [cur_grid_pos[0]+2,cur_grid_pos[1]],
            [cur_grid_pos[0]+3,cur_grid_pos[1]]))
  #down
  if cur_grid_pos[1]+3 <= grid_y:
    quad_list.append((cur_grid_pos,
            [cur_grid_pos[0],cur_grid_pos[1]+1],
            [cur_grid_pos[0],cur_grid_pos[1]+2],
            [cur_grid_pos[0],cur_grid_pos[1]+3]))
  #diagonally-down
  if cur_grid_pos[0]+3 <= grid_x and cur_grid_pos[1]+3 <= grid_y:
    quad_list.append((cur_grid_pos,
            [cur_grid_pos[0]+1,cur_grid_pos[1]+1],
            [cur_grid_pos[0]+2,cur_grid_pos[1]+2],
            [cur_grid_pos[0]+3,cur_grid_pos[1]+3]))
  #diagonally-up
  if cur_grid_pos[0]+3 <= grid_x and cur_grid_pos[1]-3 <= grid_y:
    quad_list.append((cur_grid_pos,
            [cur_grid_pos[0]+1,cur_grid_pos[1]-1],
            [cur_grid_pos[0]+2,cur_grid_pos[1]-2],
            [cur_grid_pos[0]+3,cur_grid_pos[1]-3]))
  return quad_list

raw_grid_data = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08x49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00x81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65x52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91x22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80x24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50x32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70x67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21x24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72x21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95x78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92x16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57x86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58x19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40x04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66x88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69x04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36x20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16x20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54x01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

grid = process_grid_data(raw_grid_data)
grid_x_idx = len(grid[0])-1
grid_y_idx = len(grid)-1

greatest_product = 0
for x in range(0, grid_x_idx+1):
  for y in range(0, grid_y_idx+1):
    all_quad_pos = get_all_quad_pos([x,y], grid_x_idx, grid_y_idx)
    if not all_quad_pos:
      continue
    for quad_pos in all_quad_pos:
      product_values = 1
      for val in quad_pos:
        product_values*= grid[val[0]][val[1]]
      if product_values>greatest_product:
        greatest_product = product_values
print greatest_product

