# display image from waymo dataset
def display_instances(batch):
    """
    This function takes a batch from the dataset and display the image with 
    the associated bounding boxes.
    """
    # ADD CODE HERE
    plt.figure()
    img = batch['image'].numpy()
    classes = batch['groundtruth_classes'].numpy()
    boxes = batch['groundtruth_boxes'].numpy()
    h,w,c = img.shape
    boxes[:,(0,2)] *= h
    boxes[:,(1,3)] *= w
    
    colormap = {1:[1,0,0],2:[0,1,0],4:[0,0,1]}
    f, ax = plt.subplots(1, figsize=(10, 10))
    ax.imshow(img.astype(np.uint8))
    for box, box_class in zip(boxes, classes):
        y1, x1, y2, x2 = box
        rec = Rectangle((x1, y1), x2-x1, y2-y1, facecolor='none', edgecolor=colormap[box_class], linewidth=2)
        ax.add_patch(rec)      
    plt.show()
    return
    
   

def plot_air_traffic_data()  

    # Create a figure with 2 rows and 2 columns of subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True, gridspec_kw={'hspace': 0.3})

    # Plot the data on the subplots
    axs[0, 0].plot(df['year'], df['passengers_to_india'], label='Passengers To India')
    axs[0, 1].plot(df['year'], df['passengers_from_india'], label='Passengers From India')
    axs[1, 0].plot(df['year'], df['freight_to_india'], label='Freight To India')
    axs[1, 1].plot(df['year'], df['freight_from_india'], label='Freight From India')

    # Add titles and axis labels for each subplot
    axs[0, 0].set_title('Passengers To India')
    axs[0, 0].set_xlabel('Year')
    axs[0, 0].set_ylabel('Number of Passengers')

    axs[0, 1].set_title('Passengers From India')
    axs[0, 1].set_xlabel('Year')
    axs[0, 1].set_ylabel('Number of Passengers')

    axs[1, 0].set_title('Freight To India')
    axs[1, 0].set_xlabel('Year')
    axs[1, 0].set_ylabel('Freight in Tons')

    axs[1, 1].set_title('Freight From India')
    axs[1, 1].set_xlabel('Year')
    axs[1, 1].set_ylabel('Freight in Tons')

    # Add a shared title for the entire figure
    fig.suptitle('Passengers and Freight over Time')

    # Show the legend and plot the chart
    for ax in axs.flat:
        ax.legend()
    plt.show()
    
    
def plot_ohlc(): 
    fig, ax = plt.subplots()
    data['Close'].plot(ax=ax)
    ax.set_ylabel("Price")
    ax.set_title("AAPL")

    fig, ax = plt.subplots(2, 2)
    data['Open'].plot(ax=ax[0, 0], title="Open")
    data['High'].plot(ax=ax[0, 1], title="High")
    data['Low'].plot(ax=ax[1, 0], title="Low")
    data['Close'].plot(ax=ax[1, 1], title="Close")
    plt.tight_layout()#