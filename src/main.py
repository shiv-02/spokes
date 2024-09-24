import aspose.slides as slides
import aspose.pydrawing as drawing
from aspose.slides import Presentation, AutoShape, Connector, GroupShape
import os

def set_license(license_path):
    """
    Set the Aspose.Slides license to remove watermarks and ensure full functionality.

    Args:
        license_path (str): Path to the license file.
    """
    try:
        license = slides.License()
        license.set_license(license_path)
        print("License set successfully.")
    except Exception as e:
        print(f"Error setting license: {e}")


def process_decks(directory_path, license_path, save_img_dir="spoke_slide_image"):
    """
    Convert each slide in all presentations in the specified directory to images and save them to the specified folder.

    Args:
        directory_path (str): Path to the directory containing presentation files.
        save_img_dir (str): Directory where the images will be saved.
        license_path (str): Path to the license file.
    """
    # Set the license
    set_license(license_path)
    
    # Get a list of all .pptx files in the directory
    ppt_files = [f for f in os.listdir(directory_path) if f.endswith('.pptx')]
    
    if not os.path.exists(save_img_dir):
        os.makedirs(save_img_dir)  # Create the directory if it doesn't exist

    for ppt_file in ppt_files:
        deck_path = os.path.join(directory_path, ppt_file)
        deck_name = os.path.splitext(ppt_file)[0]  # Get the deck name without extension
        try:
            source_prs = slides.Presentation(deck_path)
            master = source_prs.slides[0]
            slideBmp = master.get_thumbnail(1, 1)
            slideBmp.save(f'{save_img_dir}/{deck_name}.jpg',drawing.imaging.ImageFormat.jpeg)
        except Exception as e:
            print(f"Error processing presentation {deck_path}: {e}")
        # try:
        #     with slides.Presentation(deck_path) as presentation:
        #         for slide_index in range(len(presentation.slides)):
        #             slide = presentation.slides[slide_index] 
        # except Exception as e:
        #     print(f"Error processing presentation {deck_path}: {e}")


if __name__ == "__main__":
    license_path = "/data2/shiv/Aspose.Slides.Python.NET.lic"
    # Set the license
    set_license(license_path)
    # Path to your PPTX file
    directory_path = "/data2/shiv/SPOKE_PPT/spoke"
    # file_path = "/data2/shiv/layout_analysis_generation/test_ppt/test47.pptx"
    
    process_decks(directory_path, license_path)
    # file_path = "/data2/shiv/spoke_detection/src/Connecting shapes using connectors_out.pptx"

    # # Instantiates a presentation class that represents a PPTX file
    # with slides.Presentation() as input:
    #     # Accesses the shapes collection for a specific slide
    #     shapes = input.slides[0].shapes

    #     # Adds an Ellipse autoshape
    #     ellipse = shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 0, 100, 100, 100)

    #     # Adds a Rectangle autoshape
    #     rectangle = shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 300, 100, 100)

    #     # Adds a connector shape to the slide shape collection
    #     connector = shapes.add_connector(slides.ShapeType.BENT_CONNECTOR2, 0, 0, 10, 10)

    #     # Connects the shapes using the connector
    #     connector.start_shape_connected_to = ellipse
    #     connector.end_shape_connected_to = rectangle

    #     # Calls reroute that sets the automatic shortest path between shapes
    #     connector.reroute()

    #     # Saves the presentation
    #     input.save("Connecting shapes using connectors_out.pptx", slides.export.SaveFormat.PPTX)

    # with Presentation(file_path) as pres:
    #     for slide in pres.slides:
    #         for shape in slide.shapes:
    #             if isinstance(shape, GroupShape):
    #                 for ghshape in shape.shapes:
    #                     if isinstance(ghshape, Connector):
                        
    #                         # Get the connection sites
    #                         connection_site_count = ghshape.connection_site_count
    #                         print(f"Number of Connection Sites: {connection_site_count}")
                            
    #                         # Each connector shape has a start and end point
    #                         # These are determined by the connection site indices
    #                         if connection_site_count >= 0:
    #                             start_site_index = ghshape.connection_site_index_start
    #                             end_site_index = ghshape.connection_site_index_end
                                
    #                             print(f"Start Site Index: {start_site_index}")
    #                             print(f"End Site Index: {end_site_index}")
                                
    #                             # To get connected shapes, you need to inspect the connections
    #                             # This may require custom logic depending on your library's features
                                
    #                             # Note: You might need to iterate over all shapes to find which shapes are connected
    #                             connected_shapes = []
    #                             for potential_shape in ghshape.shapes:
    #                                 if potential_shape != shape and isinstance(potential_shape, ShapeType):
    #                                     if (potential_shape.connection_site_count > 0):
    #                                         # Check if this shape is connected to the connector
    #                                         # You would need to write logic to match connection sites
    #                                         connected_shapes.append(potential_shape)

    #                             print(f"Connected Shapes: {[s.id for s in connected_shapes]}")
    #                         else:
    #                             print("Connector does not have enough connection sites.")

    # # # Extract paragraphs with relationships
    # # paragraphs_relationships = extract_paragraphs_with_relationships(file_path)

    # # # Print the extracted paragraph relationships
    # # for indent_level, relationships in paragraphs_relationships.items():
    # #     print(f"Indent Level {indent_level}:")
    # #     for parent, child in relationships:
    # #         print(f"  Parent: {parent} -> Child: {child}")