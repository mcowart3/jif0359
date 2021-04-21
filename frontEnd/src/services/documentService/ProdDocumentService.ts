import IDocumentService from "./IDocumentService";
import Metadata from "../../model/Metadata";
import LitDocument from "../../model/LitDocument";
import SortBy from "../../model/SortBy";

export default class ProdDocumentService implements IDocumentService {
  public async getDocuments(): Promise<LitDocument[]> {
    let response = await fetch("http://api.lettersminglesouls.live/documents");
    let documents = await response.json();

    documents = documents.map((document) => {
      return new LitDocument(
        document._id,
        document.author,
        document.text,
        document.title,
        undefined,
        undefined,
        document.tags
      );
    });
    return new Promise((resolve, reject) => resolve(documents));
  }

  public async sortDocuments(sortBy: SortBy): Promise<LitDocument[]> {
    let documents = await (
      await fetch("http://api.lettersminglesouls.live/sort/" + sortBy.endpoint)
    ).json();
    console.log(documents);
    documents = documents.map((document) => {
      return new LitDocument(
        document._id,
        document.author,
        document.text,
        document.title,
        undefined,
        undefined,
        document.tags
      );
    });
    return new Promise((resolve, reject) => resolve(documents));
  }

  public async searchDocuments(query: string): Promise<LitDocument[]> {
    let documents = await (
      await fetch("http://api.lettersminglesouls.live/search/" + query, {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
    ).json();
    console.log(documents);
    documents = documents.map((document) => {
      return new LitDocument(
        document._id,
        document.author,
        document.text,
        document.title,
        undefined,
        undefined,
        document.tags
      );
    });
    return new Promise((resolve, reject) => resolve(documents));
  }
}
