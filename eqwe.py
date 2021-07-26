# import pygame


# def main():
#     clock = pygame.time.Clock()
#     screen = pygame.display.set_mode((640, 480))
#     font = pygame.font.Font(None, 64)
#     blue = pygame.Color('royalblue')
    
#     orig_surf = font.render('Enter your text', True, blue)
#     txt_surf = orig_surf.copy()
#     # This surface is used to adjust the alpha of the txt_surf.
#     alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
#     alpha = 255  # The current alpha value of the surface.

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return

#         if alpha > 0:
#             # Reduce alpha each frame, but make sure it doesn't get below 0.
#             alpha = max(alpha-4, 0)
#             txt_surf = orig_surf.copy()  # Don't modify the original text surf.
#             # Fill alpha_surf with this color to set its alpha value.
#             alpha_surf.fill((255, 255, 255, alpha))
#             # To make the text surface transparent, blit the transparent
#             # alpha_surf onto it with the BLEND_RGBA_MULT flag.
#             txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

#         screen.fill((30, 30, 30))
#         screen.blit(txt_surf, (30, 60))
#         pygame.display.flip()
#         clock.tick(10)


# if __name__ == '__main__':
#     pygame.init()
#     main()
#     pygame.quit()
