export interface Item {
    id: number;
    title: string;
    description: string;
    price: number;
    created_date: Date;
    updated_date: Date;
    reviews: Array<Review>;
    attachments: Array<Attachment>;
}


export interface Review {
    id: number;
    rating: number;
    title: string;
    description: string;
    created_date: Date;
}

export interface Attachment {
    image: Blob;
    base64_image: Array<string>;
    created: Date;
}